'''
Created on May 23, 2013

@author: localdad
'''

class ShipLocation(object):
    '''
    classdocs
    '''
    def __init__(self,location):
        '''
        Constructor
        '''
        self.location=location
        
    def attack(self, point):
        from com.pbw import Board
        if (point in self.location):
            self.location.remove(point)
            if (len(self.location)==0):
                return Board.Board.SUNK
            else:
                return Board.Board.HIT
        else:
            return Board.Board.MISS
        