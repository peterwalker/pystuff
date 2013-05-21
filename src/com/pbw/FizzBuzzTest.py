'''
Created on May 21, 2013

@author: localdad
'''
import unittest
from com.pbw import FizzBuzz

class FizzBuzzTest(unittest.TestCase):
    fb = FizzBuzz.FizzBuzz()
    
    def testFizzBuzz(self):
        self.check(1,"" )
        self.check(3,"Fizz" )
        self.check(5,"Buzz" )
        self.check(15,"FizzBuzz!" )

    def check(self, value, answer):
        self.assertEqual(self.fb.check(value),answer)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()