'''
Created on May 22, 2013

@author: localdad
'''
import unittest
from com.pbw import Quicksort

class QuicksortTest(unittest.TestCase):
    qs = Quicksort.Quicksort()

    def testSort(self):
        self.check([],[])         
        self.check([ 1, 0],[ 0, 1 ])  
        self.check([ 5, 5, 6, 6, 4, 4, 5, 5, 4, 4, 6, 6, 5, 5 ],[4,4,4,4,5,5,5,5,5,5,6,6,6,6])
        self.check([ 1,4,7,11,2,5,8,12,3,6,9,2],[1,2,2,3,4,5,6,7,8,9,11,12])


    def check(self,unsorted, ordered):
        self.assertEqual(self.qs.sort(unsorted),ordered)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSort']
    unittest.main()