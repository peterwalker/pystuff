'''
Created on May 22, 2013

@author: localdad
'''
import unittest
from com.pbw import Palindrome

class PalindromeTest(unittest.TestCase):
    palindrome = Palindrome.Palindrome()

    def testPalindrome(self):
        self.check("madam",True)
        self.check("Able was I ere I saw Elba",True)
        self.check("foobar",False)
    
    def check(self, phrase, isPalindrome):
        self.assertEqual(self.palindrome.isPalindrom(phrase),isPalindrome)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPalindrome']
    unittest.main()