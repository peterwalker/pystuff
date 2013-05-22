'''
Created on May 22, 2013

@author: localdad
'''
import array
class Fibonacci(object):
    cache = dict()

    def __init__(self):
        self.cache[0]=0
        self.cache[1]=1
        
    def sequence(self, value):
        sequence = array.array('l')
        for i in range (0,value+1):
            sequence.append(self.fibCalc(i))
        return sequence
             
    def fibCalc(self, value):
        result = self.cache.get(value)
        if (result!=None):
            return result
        result = self.fibCalc(value - 1) + self.fibCalc(value - 2);
        self.cache[value]=result
        return result;       