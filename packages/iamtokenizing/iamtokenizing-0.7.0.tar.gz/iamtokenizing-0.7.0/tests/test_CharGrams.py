"""
Test of the span class

Run as 

python3 -m unittest -v tests.test_CharGrams
"""

import unittest as ut

from iamtokenizing import CharGrams
from extractionstring import ExtractionString, EvenSizedSortedSet 

# # for construction
# class Empty(): pass
# self = Empty()

class TestNGrams(ut.TestCase):
    
    def test_Basics(self,):
        """Basic attributes of CharGrams object"""
        string = 'ABCDEFGH'
        chargrams = CharGrams(string=string)
        self.assertTrue(isinstance(chargrams,CharGrams))
        self.assertTrue(issubclass(CharGrams,ExtractionString))
        self.assertTrue(hasattr(chargrams,'intervals'))
        self.assertTrue(getattr(chargrams,'intervals')==EvenSizedSortedSet(0,8))
        self.assertTrue(hasattr(chargrams,'string'))
        self.assertTrue(getattr(chargrams,'string')==string)
        self.assertTrue(hasattr(chargrams,'subtoksep'))
        self.assertTrue(getattr(chargrams,'subtoksep')==' ')
        return None

    def test_CharSplitting(self,):
        """CharGrams OK"""
        string = 'ABCDEFGH'
        chargrams = CharGrams(string=string)
        chargrams.tokenize()
        self.assertTrue(len(chargrams.intervals) == 1)
        self.assertTrue(len(chargrams[:]) == 8)
        self.assertTrue(isinstance(chargrams[0],CharGrams))
        with self.assertRaises(IndexError):
            chargrams[9]
        subStrings = [c for c in string]
        self.assertTrue(len(subStrings) == len(chargrams[:]))
        for cg,ss in zip(chargrams,subStrings):
            self.assertTrue(str(cg)==ss)
        return None

    def test_BiGramsSplitting(self,):
        """2-CharGrams OK"""
        string = 'ABCDEFGH'
        chargrams = CharGrams(string=string,subtoksep='_')
        chargrams.tokenize(size=2)
        self.assertTrue(len(chargrams.intervals) == 1)
        self.assertTrue(len(chargrams[:]) == 7)
        self.assertTrue(isinstance(chargrams[0],CharGrams))
        with self.assertRaises(IndexError):
            chargrams[8]
        subStrings = [s1+s2 for s1,s2 in zip(string[:-1],string[1:])]
        self.assertTrue(len(subStrings) == len(chargrams[:]))
        for cg,ss in zip(chargrams,subStrings):
            self.assertTrue(str(cg)==ss)
        return None

    def test_ThreeGramsSplittingStep(self,):
        """3-CharGrams with step=2 OK"""
        string = 'ABCDEFGH'
        chargrams = CharGrams(string=string,subtoksep='_')
        chargrams.tokenize(size=3,step=2)
        self.assertTrue(len(chargrams.intervals) == 1)
        self.assertTrue(len(chargrams[:]) == 3)
        self.assertTrue(isinstance(chargrams[0],CharGrams))
        with self.assertRaises(IndexError):
            chargrams[4]
        subStrings = [s1+s2+s3 for s1,s2,s3 in zip(string[:-2:2],string[1::2],string[2::2])]
        self.assertTrue(len(subStrings) == len(chargrams[:]))
        for cg,ss in zip(chargrams,subStrings):
            self.assertTrue(str(cg)==ss)
        return None    
    
    def test_Recurence(self,):
        """Test the recursion into tokens"""
        string = "ABCDEFGH"
        chargrams = CharGrams(string=string)
        chargrams.tokenize(size=2)
        subStrings = [s1+s2 for s1,s2 in zip(string[:-1],string[1:])]
        self.assertTrue(str(chargrams[0]) == subStrings[0])
        self.assertTrue(chargrams[0].intervals == EvenSizedSortedSet(0, 2))
        self.assertTrue(str(chargrams[1]) == subStrings[1])
        self.assertTrue(chargrams[1].intervals == EvenSizedSortedSet(1, 3))
        chargrams[0].tokenize()
        for i in range(len(chargrams[0].to_strings())):
            self.assertTrue(chargrams[0].to_strings()[i] == subStrings[0][i])
        return None
    
if __name__ == '__main__':
    ut.main()
