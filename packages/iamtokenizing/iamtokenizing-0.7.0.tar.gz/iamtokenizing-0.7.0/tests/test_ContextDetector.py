"""
Test of the ContextDetector class

Run as 

python3 -m unittest -v tests.test_ContextDetector
"""

import unittest as ut

from iamtokenizing import ContextDetector
from extractionstring import ExtractionString, EvenSizedSortedSet

# # for construction
# class Empty(): pass
# self = Empty()

class TestContextDetector(ut.TestCase):
    
    def test_Basics(self,):
        """Basic attributes of ContextDetector object"""
        string = 'A B C D E F G H'
        contdet = ContextDetector(string=string)
        self.assertTrue(isinstance(contdet,ContextDetector))
        self.assertTrue(issubclass(ContextDetector,ExtractionString))
        self.assertTrue(hasattr(contdet,'intervals'))
        self.assertTrue(getattr(contdet,'intervals')==EvenSizedSortedSet(0, 15))
        self.assertTrue(hasattr(contdet,'string'))
        self.assertTrue(getattr(contdet,'string')==string)
        self.assertTrue(hasattr(contdet,'subtoksep'))
        self.assertTrue(getattr(contdet,'subtoksep')==' ')
        return None

    def test_Tokenization(self,):
        """Word tokenization OK"""
        string = "test of 0 string\n test 1 and 2 then 3 STRING\n test without digit\n4 beginning token\nending token 5"
        intervals = [8,9, 23,24, 29,30, 36,37, 65,66, 96,97]
        contdet = ContextDetector(string=string)
        contdet.tokenize()
        self.assertTrue(len(contdet.intervals) == 6)
        self.assertTrue(isinstance(contdet[0],ContextDetector))
        with self.assertRaises(IndexError):
            contdet[7]
        self.assertTrue(contdet.intervals.list == intervals)
        self.assertTrue(str(contdet.context) == ' '.join(string.split('\n')))
        self.assertTrue(str(contdet[0].context_left) == string[0:8])
        self.assertTrue(str(contdet[0]) == string[8:9])
        self.assertTrue(str(contdet[0].context_right) == string[9:16])
        self.assertTrue(str(contdet[1].context_left) == string[17:23])
        self.assertTrue(str(contdet[1]) == string[23:24])
        self.assertTrue(str(contdet[1].context_right) == string[24:29])
        self.assertTrue(str(contdet[2].context_left) == string[24:29])
        self.assertTrue(str(contdet[2]) == string[29:30])
        self.assertTrue(str(contdet[2].context_right) == string[30:36])
        self.assertTrue(str(contdet[3].context_left) == string[30:36])
        self.assertTrue(str(contdet[3]) == string[36:37])
        self.assertTrue(str(contdet[3].context_right) == string[37:44])
        self.assertTrue(str(contdet[4].context_left) == string[65:65])
        self.assertFalse(bool(contdet[4].context_left))
        self.assertTrue(str(contdet[4]) == string[65:66])
        self.assertTrue(str(contdet[4].context_right) == string[66:82])
        self.assertTrue(str(contdet[5].context_left) == string[83:96])
        self.assertTrue(str(contdet[5]) == string[96:97])
        self.assertTrue(str(contdet[5].context_right) == string[97:97])
        self.assertFalse(bool(contdet[5].context_right))
        return None
    
    def test_Tokenization_empty_regdet(self,):
        """ContextDetector when there is no detection in the entire document"""
        string = "test of string\nwithout digit"
        contdet = ContextDetector(string)
        contdet.tokenize()
        self.assertEqual(contdet.string, string)
        self.assertEqual(contdet.intervals, [])
        contdet.tokenize()
        self.assertEqual(contdet.string, string)
        self.assertEqual(contdet.intervals, [])
        contdet = ContextDetector(string)
        cd = contdet.tokenize(inplace=False)
        self.assertEqual(cd.string, string)
        self.assertEqual(cd.intervals, [])
        self.assertEqual(cd.context_left, None)
        self.assertEqual(cd.context_right, None)
        return None
        
if __name__ == '__main__':
    ut.main()
