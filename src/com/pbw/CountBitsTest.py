'''
Created on May 22, 2013

@author: localdad
'''
import unittest
from com.pbw import BitCounter

class CountBits(unittest.TestCase):
    bc = BitCounter.BitCounter()

    def testBits(self):
        self.check(0,0)
        self.check(1,1)
        self.check(1,1)
        self.check(7,3)
        self.check(8,1)
        self.check(9,2)
        self.check(2147483647,31)
        
    def check(self, value, bits ):
        self.assertEqual(self.bc.countBits(value),bits)
        self.assertEqual(self.bc.fastBits(value),bits)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBits']
    unittest.main()