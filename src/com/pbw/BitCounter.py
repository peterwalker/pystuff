'''
Created on May 22, 2013

@author: localdad
'''
import array

class BitCounter(object):
    '''
    classdocs
    '''
    bitMap = array.array('i')

    def __init__(self):
        '''
        Constructor
        '''
        self.populateBitMap()
        
    def populateBitMap(self):
        for i in range(0,65536):
            self.bitMap.append(self.countBits(i));
        
    def countBits(self, value):
        count = 0
        while (value > 0):
            x = ( value & 1 )
            if (x == 1):
                count+=1    
            value >>= 1
        return count
    
    def fastBits(self, value):
        highValueBits = value >> 16
        lowValueBits = value & 0x0000FFFF
        bitCount = self.bitMap[lowValueBits] + self.bitMap[highValueBits]
        return bitCount
