'''
Created on May 22, 2013

@author: localdad
'''
import array
class Fibonacci(object):
    cache = array.array('l')
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.cache.append(0)
        self.cache.append(1)
        
    def sequence(self, value):
        sequence = array.array('l')
        for i in range (0,value+1):
            sequence.append(self.fibCalc(i))
        return sequence
             
    def fibCalc(self, value):
        if (value==0):
            return 0;
        if (value==1):
            return 1;
        result = self.fibCalc(value - 1) + self.fibCalc(value - 2);
        return result;       