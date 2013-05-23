'''
Created on May 23, 2013

@author: localdad
'''
from com.pbw import ShipLocation
class Board(object):
    '''
    classdocs
    '''
    class HIT:pass
    class MISS:pass
    class SUNK:pass

    def __init__(self, size):
        '''
        Constructor
        '''
        self.size=size
        self.shipLocations=[]
        
    def addShipLocation(self, location):
        self.shipLocations.append(ShipLocation.ShipLocation(location))
        
    def attack(self, point):
        for shipLocation in self.shipLocations:
            result = shipLocation.attack(point);
            if (result == Board.HIT or result == Board.SUNK):
                return result
        return Board.MISS    