#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ContextTokenization class allows to tokenize a part of a string into a context.
The context is the left and right parts around a token.
"""
import re
from typing import Union
from .base_tokenizer import BaseTokenizer, EvenSizedSortedSet
from . import NGrams
from . import RegexDetector

class ContextDetector(BaseTokenizer):
    """
ContextDetector class allows splitting of a big text into chunks given by the `splitter` REGEX parameter of the `tokenize` method, then it detects the `selector` REGEX  inside each chunk, and associates the context to each of the detection. The context are given by the sub-strings in between different detections. By default `ContextDetector` detects digits inside sentence (or paragraph, that is, part of the string separated by newline character).
    """

    def __init__(self,
                 string: str = str(),
                 subtoksep: chr = chr(32),
                 intervals: Union[None, EvenSizedSortedSet] = None,
                 ):
        """
ContextDetector has all the parameters of a Span object, namely `string` (the string to be tokenized), a `subtoksep` that will be inserted between the different sub-tokens of a Span object (default is a free space), and a list of `intervals`. 

The different attributes will store : 
    - `context`: all the NGrams that represent the splitter selection (macro token)
    - `tokens` : all the ContextDetector.s instances that represent the selector selection (micro token)
    - `context_left`: the NGrams left to the ContextDetector token
    - `context_right`: the NGrams right to the ContextDetector token
    - `context_parent`: the parent NGrams that corresponds to the local context
    - `position`: the position of the detected token inside the context
        """
        if isinstance(string, ContextDetector):
            args = {k:v for k,v in string.__dict__.items() 
                    if k in ['string', 'subtoksep', 'ranges']}
        else:
            args = {'string': string, 'subtoksep': subtoksep, 'intervals': intervals}
        BaseTokenizer.__init__(self, **args)
        self.context = None
        self.context_left = None
        self.context_right = None
        self.context_parent = None
        self.tokens = []
        return None
    
    def __call__(self, 
                 string=str(),
                 subtoksep=chr(32),
                 intervals=None,
                 splitter='\n+', 
                 selector='\d+',
                 splitter_flags=0,
                 selector_flags=0):
        """
Apply the `.tokenize` method to a new string. Returns a new `ContextDetector` instance. All parameters from `ContextDetector` and/or `ContextDetector.tokenize` are available, except `inplace`, which is always `False`.
        """
        ct = ContextDetector(string=str(string),
                             subtoksep=subtoksep,
                             intervals=intervals)
        return ct.tokenize(splitter=splitter,
                           selector=selector,
                           splitter_flags=0,
                           selector_flags=0,
                           inplace=False)
    
    def _append_token(self, position, context_parent, detection, start, stop):
        """Append a ContextDetector to the tokens attribute"""
        ct = ContextDetector(detection)
        ct.context_parent = position
        try:
            start_esss = EvenSizedSortedSet(start, detection.start)
        except ValueError:
            start_esss = EvenSizedSortedSet()
        ct.context_left = NGrams(string=detection.string,
                                 intervals=start_esss,
                                 subtoksep=detection.subtoksep)
        try:
            stop_esss = EvenSizedSortedSet(detection.stop, stop)
        except ValueError:
            stop_esss = EvenSizedSortedSet()
        ct.context_right = NGrams(string=detection.string,
                                  intervals=stop_esss,
                                  subtoksep=detection.subtoksep)
        self.tokens.append(ct)
        return None
    
    def _several_detections(self, position, context, detections):
        """Constructs the different tokens in case there are more than one detections"""
        start = context.start
        for detection1, detection2 in zip(detections[:-1], detections[1:]):
            self._append_token(position, context, detection1, start, detection2.start)
            start = detection1.stop
        self._append_token(position, context, detection2, start, context.stop)
        return None
    
    def tokenize(self, 
                 splitter: Union[str, bytes] = r'\n+', 
                 selector: Union[str, bytes] = r'\d+', 
                 inplace: bool = True,
                 splitter_flags: Union[re.RegexFlag, int] = 0,
                 selector_flags: Union[re.RegexFlag, int] = 0):
        """
Detects the `selector` REGEX inside the parent string and associate a context to each detection, the context being given by the remaining parts of the tokens given by the `splitter` REGEX expressions.
`selector` uses the `RegexDetector` tokenization, and `splitter` uses the `NGrams` tokenization.

        Parameters
        ----------
        splitter : Union[str, bytes], optional
            The REGEX that will be used to split the complete string into context sub-strings.. The default is '\\n+'.
        splitter_flags : Union[re.RegexFlag, int], optional
            The flags that will be transmitted to the `NGrams.tokenize` method of the splitting. flags are inherited from `re` package, and can be combined using a pipe symbol, for instance `flags=re.DOTALL|re.MULTILINE` apply both DOTALL (special character '.' also accepts new line) and MULTILINE (special characters '^' and '$' match begining and end of each new line). By default `splitter_flags=0`.The default is 0.
        selector : Union[str, bytes], optional
            The REGEX that will be used to detect a part of the context string. The default is '\\d+'.
        selector_flags : Union[re.RegexFlag, int], optional
            The flags that will be transmmitted to the `RegexDetector.tokenize` method of the detection. flags are inherited from `re` package, and can be combined using a pipe symbol, for instance `flags=re.DOTALL|re.MULTILINE` apply both DOTALL (special character '.' also accepts new line) and MULTILINE (special characters '^' and '$' match begining and end of each new line). The default is 0.
        inplace : bool, optional
            Whether the method changes the object in place (`inplace=True`, by default) or returns a new object. The default is True.

See the user guide for more details.
        """
        self.tokens = []
        if not inplace:
            self = self.__class__(self)
        contexts = NGrams(self)
        self.context = contexts.tokenize(regex=splitter, 
                                         inplace=False, 
                                         flags=splitter_flags)
        intervals_ = []
        for position, context in enumerate(self.context):
            detections = RegexDetector(context)
            detections = detections.tokenize(regex=selector, 
                                             inplace=False, 
                                             flags=selector_flags)
            intervals_.extend(detections.intervals.list)
            if len(detections.tokens) == 1:
                # works since detections.start = detections.intervals[0].start
                # and detections.stop = detections.intervals[-1].stop
                # and len(detections.intervals) == 1
                self._append_token(position, context, detections,
                                   context.start, context.stop)
            elif len(detections.tokens) > 1:
                self._several_detections(position, context, detections)
        self.intervals = EvenSizedSortedSet(*intervals_) 
        return self

