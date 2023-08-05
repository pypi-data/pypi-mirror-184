"""
Test of the span class

Run as 

python3 -m unittest -v tests.test_RegexDetector
"""

import unittest as ut

from iamtokenizing import RegexDetector
from extractionstring import ExtractionString, EvenSizedSortedSet

# # for construction
# class Empty(): pass
# self = Empty()

class TestNGrams(ut.TestCase):
    
    def test_Basics(self,):
        """Basic attributes of rgrams object"""
        string = 'ABCDEFGH'
        rgrams = RegexDetector(string=string)
        self.assertTrue(isinstance(rgrams,RegexDetector))
        self.assertTrue(issubclass(RegexDetector,ExtractionString))
        self.assertTrue(hasattr(rgrams,'intervals'))
        self.assertTrue(getattr(rgrams,'intervals')==EvenSizedSortedSet(0, 8))
        self.assertTrue(hasattr(rgrams,'string'))
        self.assertTrue(getattr(rgrams,'string')==string)
        self.assertTrue(hasattr(rgrams,'subtoksep'))
        self.assertTrue(getattr(rgrams,'subtoksep')==' ')
        return None

    def test_Tokenization(self,):
        """rgrams OK"""
        string = 'ABCDEFGH'
        rgrams = RegexDetector(string=string)
        rgrams.tokenize(regex='ABC')
        self.assertTrue(len(rgrams.intervals) == 1)
        self.assertTrue(len(rgrams[:]) == 1)
        self.assertTrue(isinstance(rgrams[0],RegexDetector))
        with self.assertRaises(IndexError):
            rgrams[1]
        subStrings = ['ABC',]
        self.assertTrue(len(subStrings) == len(rgrams[:]))
        for rg,ss in zip(rgrams,subStrings):
            self.assertTrue(str(rg)==ss)
        return None 
    
    def test_Recurence(self,):
        """Test the recursion into tokens"""
        string = "ABCDEFGH"
        rgrams = RegexDetector(string=string)
        rgrams.tokenize(regex='ABC')
        subStrings = ['ABC',]
        self.assertTrue(str(rgrams[0]) == subStrings[0])
        self.assertTrue(rgrams[0].intervals == EvenSizedSortedSet(0, 3))
        rgrams[0].tokenize(regex='B')
        self.assertTrue(rgrams[0].to_strings()[0] == 'B')
        self.assertTrue(rgrams[0].intervals == EvenSizedSortedSet(1, 2))
        return None
    
    def test_Inplace(self,):
        """Test the inplace parameter"""
        string = "ABCDEFGH"
        rgrams = RegexDetector(string=string)
        rgrams_ = rgrams.tokenize(regex='ABC', inplace=False)
        subStrings = ['ABC',]
        self.assertTrue(str(rgrams_[0]) == subStrings[0])
        self.assertTrue(len(rgrams_[:]) == 1)
        self.assertTrue(rgrams_[0].intervals == EvenSizedSortedSet(0, 3))
        self.assertTrue(rgrams.tokens == [])
        rgrams.tokenize(regex='ABC')
        self.assertTrue(str(rgrams[0]) == subStrings[0])
        self.assertTrue(len(rgrams[:]) == 1)
        self.assertTrue(rgrams[0].intervals == EvenSizedSortedSet(0, 3))
        return None    
    
if __name__ == '__main__':
    ut.main()
