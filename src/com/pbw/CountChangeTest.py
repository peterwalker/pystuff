'''
Created on May 21, 2013

@author: localdad
'''
import unittest
from com.pbw import ChangeCounter

class Test(unittest.TestCase):
    cc = ChangeCounter.ChangeCounter()

    def testCountChange(self):
        self.check(0,0,0,0,0)
        self.check(0.25,1,0,0,0)
        self.check(0.26,1,0,0,1)
        self.check(0.27,1,0,0,2)
        self.check(0.28,1,0,0,3)
        self.check(0.29,1,0,0,4)
        self.check(0.30,1,0,1,0)
        self.check(0.35,1,1,0,0)
        self.check(1.01,4,0,0,1)
            
    def check(self, amount, quarters , nickels, dimes, pennies ):
        change = self.cc.countChange(amount)
        self.assertEqual(change.quarters,quarters)
        self.assertEqual(change.nickels,nickels)
        self.assertEqual(change.dimes,dimes)
        self.assertEqual(change.pennies,pennies)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCountChange']
    unittest.main()