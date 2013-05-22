'''
Created on May 22, 2013

@author: localdad
'''

class BinarySearch(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def find (self, items, value):
        left = 0
        right = len(items)-1
        while (left <= right):
            middle = ((left + right) / 2);
            if (value == items[middle]):
                return (middle)
            if (value>items[middle]):
                left = middle+1
            else:
                right = middle-1
        return -1