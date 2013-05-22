'''
Created on May 22, 2013

@author: localdad
'''
import unittest
from com.pbw import BinarySearch

class BinarySearchTest(unittest.TestCase):
    bst = BinarySearch.BinarySearch()

    def testSearch(self):
        self.check([0, 1], 2, -1)
        self.check([], 0, -1)
        self.check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],9,8)
        
    def check(self, sortedArray, value, index):
        self.assertEqual(self.bst.find(sortedArray,value),index)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSearch']
    unittest.main()