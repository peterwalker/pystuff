'''
Created on May 22, 2013

@author: localdad
'''

class Palindrome(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def isPalindrom(self, phrase):
        reversedphrase = self.rev(phrase)
        return phrase.lower()==reversedphrase.lower()
    
    def rev(self, s): return s[::-1]