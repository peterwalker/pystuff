'''
Created on May 23, 2013

@author: localdad
'''

class Point(object):
    '''
    classdocs
    '''
    def __init__(self,x,y):
        '''
        Constructor
        '''
        self.x=x
        self.y=y

    def __hash__(self):
        prime = 31
        result = 1;
        result = prime * result + self.x
        result = prime * result + self.y
        return result
    
    def __eq__(self,other):
        if (self.x != other.x):
            return False
        if (self.y != other.y):
            return False
        return True