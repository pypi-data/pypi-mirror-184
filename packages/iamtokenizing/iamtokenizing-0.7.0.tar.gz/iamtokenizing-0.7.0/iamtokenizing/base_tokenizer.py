#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BaseTokenizer is a generic class making tools for later definition of more elaborated tokenizers. It deals only with the representation, and the way the `tokens` of each children-classes are parsed by the `__getitem__` magic method.
"""
from typing import Union
from extractionstring import ExtractionString, EvenSizedSortedSet

class BaseTokenizer(ExtractionString):
    """
Define some standard functions for conversion from elaborated Tokenizer to Span, Token and Tokens classes. In sub-classes that inherits from this one, one should define a `_name_` attribute (that will be displayed on `__repr__`) and a `_subtokens_` entity that consists in a list of sub-entities that can be converted to `ExtractionString` or `String`.
    """
    
    def __init__(self, 
                 string: str = str(),
                 subtoksep: chr = chr(32),
                 intervals: Union[None, EvenSizedSortedSet] = None,
                 tokens: list = list()):
        """BaseTokenizer has the same attribute than a Span object : 
            - `string`: the string of the parent text,
            - `subtoksep`: the character that glues several sub-tokens together,
            - `ranges`: a collection of range, defining the sub-tokens position inside the string

In addition, there is the `tokens` attributes, that collects the sub-tokens once the tokenization is performed.
            """
        if isinstance(string, BaseTokenizer):
            kwargs = {k: string.__dict__[k] for k in ['string', 'subtoksep',
                                                      'intervals', 'tokens']}
        else:
            kwargs = {'string': string,
                      'subtoksep': subtoksep,
                      'intervals': intervals,
                      'tokens': tokens}
        self.__init(**kwargs)
        return None
    
    def __init(self, **kwargs):
        """The `tokens` attribute is always instanciated with an empty list. The only way to fill this list is via `.tokenize` method."""
        super().__init__(string=kwargs['string'],
                         intervals=kwargs['intervals'],
                         subtoksep=kwargs['subtoksep'])
        self.tokens = []
        return None
    
    def tokenize(self, inplace=True):
        """Main method of the class. To be overwritten by the children classes."""
        raise NotImplementedError
    
    def __getitem__(self, n):
        """Returns the n element (eventually a slice) of the tokenizer, once the method `tokenize` has been applied. Requires that the tokenizer has the attribute `_subtokens_`."""
        return self.tokens[n]
    
    def to_strings(self):
        """
Once `tokenize` method has been applied, this method transforms the `_subtokens_` list into a list of strings. 

Returns a list of strings.
        """
        return tuple(str(subtok) for subtok in self)
    
    def copy(self,):
        """Generates a new instance of the object, with the same attributes as the actual one."""
        return self.__class__(string=self.string,
                              subtoksep=self.subtoksep,
                              intervals=self.intervals.copy(),
                              tokens=self.tokens.copy())
