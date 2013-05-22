'''
Created on May 22, 2013

@author: localdad
'''
import unittest
import array
from com.pbw import Fibonacci

class FibonacciTest(unittest.TestCase):
    fibonacci = Fibonacci.Fibonacci()

    def testFibonacci(self):
        self.check(0,array.array('l',[0]))
        self.check(1,array.array('l',[0, 1]))
        self.check(2,array.array('l',[0, 1, 1]))
        self.check(3,array.array('l',[0, 1, 1, 2]))
        self.check(4,array.array('l',[0, 1, 1, 2, 3]))
        self.check(5,array.array('l',[0, 1, 1, 2, 3, 5]))  
        
    def check(self, value, sequence):
        fib = self.fibonacci.sequence(value)
        self.assertEqual(fib,sequence)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFibonacci']
    unittest.main()