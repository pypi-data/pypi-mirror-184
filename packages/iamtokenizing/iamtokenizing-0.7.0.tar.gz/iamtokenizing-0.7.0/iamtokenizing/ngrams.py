#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
NGrams class cuts a text on the space (or any other regular expression pattern), and returns the associated tokens (that are words, bigrams, paragraphs, ...) in a list of Span objects, or a list of strings, or a Tokens instance.
"""

import re
from typing import Union
from .base_tokenizer import BaseTokenizer, EvenSizedSortedSet

class NGrams(BaseTokenizer):
    """
NGrams is a sub-class of Span. It allows cutting the text (given as string parameter) on the space (whatever its length, a space can also be a newline or a tabulation), and extracting the words in between these spaces. One can change the regular expression (REGEX) in order to cut the parent string into different Span objects. For instance

Examples
--------

>>> s = "A-B-C-D"
>>> NGrams(s,regex='-').tokenize().to_strings()
# -> ['A', 'B', 'C', 'D']

would split the initial string into its constituents after cutting the string on the `'-'` symbol, and returns a list of the sub-strings (one would have obtained the same thing using `s.split('-')`.
                                                                                                                                         Other basic examples are
                                                                                                                                         
>>> s = "A-B-C-D"
>>> NGrams(s,regex='-').tokenize(2).to_strings()
# -> ['A B', 'B C', 'C D']

>>> NGrams(s,regex='-',subtoksep='@').tokenize(2).to_strings()
# -> ['A@B', 'B@C', 'C@D']

>>> NGrams(s,regex='-',subtoksep='@').tokenize(2).ngrams
# -> [NGrams('A@B', [(0,1),(2,3)]),
#     NGrams('B@C', [(2,3),(4,5)]),
#     NGrams('C@D', [(4,5),(6,7)])] # a list of NGrams objects

>>> NGrams(s,regex='-',subtoksep='@').tokenize(2).to_tokens()
# -> Tokens(3 Token) : A@B  B@C  C@D # a Tokens object

The main interests in the NGrams class is to extract into Tokens objects, or Span objects the different tokens, in order to continue working on them.

By default

>>> s = "A    B \t C  \n D"
>>> NGrams(s).tokenize().to_strings()
# -> ['A', 'B', 'C', 'D']
```
    """
    
    def __call__(self,
                 string: str = str(),
                 subtoksep: chr = chr(32),
                 intervals: Union[None, EvenSizedSortedSet] = None,
                 ngram: int = 1,
                 regex: Union[str, bytes] = r'\s+',
                 flags: Union[re.RegexFlag, int] = 0):
        """
Apply the `.tokenize` method to a new string. Returns a new `NGrams` instance. All parameters from `NGrams` and/or `NGrams.tokenize` are available, except `inplace`, which is always `False`.
        """
        ng = self.__class__(string=string,
                            subtoksep=subtoksep,
                            intervals=intervals)
        return ng.tokenize(ngram=ngram, regex=regex, flags=flags, inplace=False)
    
    def tokenize(self,
                 ngram: int = 1,
                 regex: Union[str, bytes] = r'\s+',
                 flags: Union[re.RegexFlag, int] = 0 ,
                 inplace: bool = True):
        """
Tokenize the parent string into tokens, that are themselves instances of `NGrams`.
Returns the `NGrams` object itself (tokenize is an in-place operation if `inplace=True`), or a new `NGrams` object. The different tokens are then stored in `NGrams.tokens` list.

When `ngram=1` and the used REGEX produces non-overlapping extractions, the list of `NGrams` in `NGrams.tokens` can be thought as the sub-parts given by each individual interval in the resulting `NGrams`. Otherwise the objects are not the same, and the extracted tokens are in `NGrams.tokens` list only.

        Parameters
        ----------
        ngram : int, optional
            The number of regular expression (`regex` parameter) that is withdraw in between two ngrams. In the default settings, `ngram=1` extracts words, `ngram=2` extracts bi-grams,. The default is 1.
        regex : Union[str, bytes], optional
            A regular expression (REGEX) that will serve to identify the Token to be find. The default is '\\s+'.
        flags : Union[re.RegexFlag, int], optional
            Flags are inherited from `re` package, and can be combined using a pipe symbol, for instance `flags=re.DOTALL|re.MULTILINE` apply both DOTALL (special character '.' also accepts new line) and MULTILINE (special characters '^' and '$' match begining and end of each new line). The default is 0.
        inplace : bool, optional
            Whether the method changes the object in place (`inplace=True`, by default) or returns a new object. The default is True.

By default there is no flags (that is `flags=0`) and the `regex` is on space characters (that is `regex='\s+'`). In that case, `NGrams.tokenize().to_strings()` return words in a list (eventually the punctuations are glued to the string, e.g. `A string.` returns `['A', 'string.']`).
        """
        if not inplace:
            self = self.__class__(self)
        removes = []
        for start, stop in self.intervals:
            for r in re.finditer(regex,
                                 self.string[start:stop],
                                 flags=flags):
                removes.append(start+r.start())
                removes.append(start+r.end())
        # remove the edges when they are the same (stop[i-1]==start[i])
        while len(set(removes)) < len(removes):
            removes = removes[:1] \
                + [i for i,j in zip(removes[1::2], removes[2::2]) if i!=j] \
                + [j for i,j in zip(removes[1::2], removes[2::2]) if i!=j] \
                + removes[-1:]
            removes = sorted(removes)
        self.intervals.remove_intervals(*removes)
        if ngram==1:
            self.tokens = self.extractions
            return self
        # deal with the ngrams 
        sub_tokens = self.extractions
        self.tokens = []
        for i in range(len(sub_tokens)-ngram+1):
            intervals = []
            for tok in sub_tokens[i:i+ngram]:
                intervals.append(tok.start)
                intervals.append(tok.stop)
            ngram_ = self.__class__(string=self.string,
                                    intervals=intervals,
                                    subtoksep=self.subtoksep)
            self.tokens.append(ngram_)
        return self
