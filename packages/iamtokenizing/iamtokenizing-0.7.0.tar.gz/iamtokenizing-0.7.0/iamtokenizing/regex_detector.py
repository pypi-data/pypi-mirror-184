#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RegexDetector class cuts a text on any regular expression pattern, and returns the associated tokens in a list of Span objects, or a list of strings, or a Tokens instance.
"""

import re
from typing import Union
from .base_tokenizer import BaseTokenizer, EvenSizedSortedSet

class RegexDetector(BaseTokenizer):
    """
RegexDetector is a sub-class of Span. It allows cutting the text (given as string parameter) on any regular expression (REGEX), and extracting the resulting tokens from the parent string. The tokenized objects are themselves instances of RegexDetector, and one can thus applies REGEX expression recursively in the parent string.
    """
    
    def __call__(self,
                 string: str = str(),
                 subtoksep: chr = chr(32),
                 intervals: Union[None, EvenSizedSortedSet] = None,
                 regex: Union[str, bytes] = r'\w+',
                 flags: Union[re.RegexFlag, int] = 0):
        """
Apply the `.tokenize` method to a new string. Returns a new `RegexDetector` instance. All parameters from `RegexDetector` and/or `RegexDetector.tokenize` are available, except `inplace`, which is always `False`.    
        """
        rd = self.__class__(string=string,
                            subtoksep=subtoksep,
                            intervals=intervals)
        return rd.tokenize(regex=regex, flags=flags, inplace=False)
    
    def tokenize(self, 
                 regex: Union[str, bytes] = r'\w+',
                 flags: Union[re.RegexFlag, int] = 0,
                 inplace: bool = True):
        """
Tokenize the parent string into tokens, that are themselves instances of RegexDetector (so for instance each of these instance can be searched by REGEX as well).
Returns the RegexDetector object itself (tokenize is an in-place operation if `inplace=True`), or a new RegexDetector object. The different tokens are then stored in RegexDetector.subSpans list.

        Parameters
        ----------
        regex : Union[str, bytes], optional
            A regular expression (REGEX) that will serve to identify the Token to be find. The default is '\\w+'.
        flags : Union[re.RegexFlag, int], optional
            Flags are inherited from `re` package, and can be combined using a pipe symbol, for instance `flags=re.DOTALL|re.MULTILINE` apply both DOTALL (special character '.' also accepts new line) and MULTILINE (special characters '^' and '$' match begining and end of each new line). The default is 0.
        inplace : bool, optional
            Whether the method changes the object in place (`inplace=True`, by default) or returns a new object.. The default is True.

By default there is no flags (that is `flags=0`) and the `regex` is on contiguous alpha-numeric characters (that is `regex='\\w+'`). In that case, `RegexDetector.tokenize().toStrings()` return words in a list.
        """
        if not inplace:
            self = self.__class__(self)
        intervals = []
        for start, stop in self.intervals:
            for r in re.finditer(regex,
                                 self.string[start:stop],
                                 flags=flags):
                intervals.append(start+r.start())
                intervals.append(start+r.end())
        self.tokens = [self.__class__(string=self.string,
                                      subtoksep=self.subtoksep,
                                      intervals=EvenSizedSortedSet(i,j))
                       for i,j in zip(intervals[:-1:2], intervals[1::2])]
        # remove the edges when they are the same (stop[i-1]==start[i])                
        while len(set(intervals)) < len(intervals):
            intervals = intervals[:1] \
                + [i for i,j in zip(intervals[1::2],intervals[2::2]) if i!=j] \
                + [j for i,j in zip(intervals[1::2],intervals[2::2]) if i!=j] \
                + intervals[-1:]
            intervals = sorted(intervals)                
        self.intervals = EvenSizedSortedSet(*intervals) 
        return self
