"""
Test of the span class

Run as 

python3 -m unittest -v tests.test_NGrams
"""

import unittest as ut

from iamtokenizing import NGrams
from extractionstring import ExtractionString, EvenSizedSortedSet

# # for construction
# class Empty(): pass
# self = Empty()

class TestNGrams(ut.TestCase):
    
    def test_Basics(self,):
        """Basic attributes of NGrams object"""
        string = 'A B C D E F G H'
        ngrams = NGrams(string=string)
        self.assertTrue(isinstance(ngrams,NGrams))
        self.assertTrue(issubclass(NGrams,ExtractionString))
        self.assertTrue(hasattr(ngrams,'intervals'))
        self.assertTrue(getattr(ngrams,'intervals')==EvenSizedSortedSet(0, 15))
        self.assertTrue(hasattr(ngrams,'string'))
        self.assertTrue(getattr(ngrams,'string')==string)
        self.assertTrue(hasattr(ngrams,'subtoksep'))
        self.assertTrue(getattr(ngrams,'subtoksep')==' ')
        return None

    def test_WordSplitting(self,):
        """Word tokenization OK"""
        string = 'A B C D E F G H'
        ngrams = NGrams(string=string)
        ngrams.tokenize()
        self.assertTrue(len(ngrams.intervals) == 8)
        self.assertTrue(isinstance(ngrams[0],NGrams))
        with self.assertRaises(IndexError):
            ngrams[9]
        subStrings = string.split()
        for ng,ss in zip(ngrams,subStrings):
            self.assertTrue(str(ng)==ss)
        return None

    def test_BiGramsSplitting(self,):
        """Word tokenization bigrams OK"""
        string = 'A B C D E F G H'
        ngrams = NGrams(string=string, subtoksep='_')
        ngrams.tokenize(ngram=2)
        self.assertTrue(len(ngrams.intervals) == 8)
        self.assertTrue(len(ngrams[:]) == 7)
        self.assertTrue(isinstance(ngrams[0],NGrams))
        with self.assertRaises(IndexError):
            ngrams[8]
        subStrings = string.split()
        subStrings = [s1+'_'+s2 for s1,s2 in zip(subStrings[:-1],subStrings[1:])]
        self.assertTrue(len(subStrings) == len(ngrams[:]))
        for ng,ss in zip(ngrams,subStrings):
            self.assertTrue(str(ng)==ss)
        return None
    
    def test_Recurence(self,):
        """Test the recursion into tokens"""
        string = "arc-en-ciel magique"
        ngrams = NGrams(string=string)
        ngrams.tokenize()
        string_split = string.split()
        self.assertTrue(str(ngrams[0]) == string_split[0])
        self.assertTrue(ngrams[0].intervals == EvenSizedSortedSet(0, 11))
        self.assertTrue(str(ngrams[1]) == string_split[1])
        self.assertTrue(ngrams[1].intervals == EvenSizedSortedSet(12, 19))
        ngrams[0].tokenize(regex='-')
        self.assertEqual(list(ngrams[0].to_strings()), string_split[0].split('-'))
        return None
    
if __name__ == '__main__':
    ut.main()
