'''
Created on May 21, 2013

@author: localdad
'''

class FizzBuzz(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def check(self, value):
        result = ""
        if (value % 3 == 0 and value % 5 == 0) :
            result = "FizzBuzz"
        elif (value % 3 == 0) :
            result = "Fizz"
        elif (value % 5 == 0) :
            result = "Buzz"
        return result