'''
Created on May 23, 2013

@author: localdad
'''
import unittest
from com.pbw import Board
from com.pbw import Point

class Test(unittest.TestCase):

    def testSinkOneShip(self):
        b = Board.Board(1)
        p = Point.Point(0,0)
        location = set([Point.Point(0,0)])
        b.addShipLocation(location)
        
        self.assertEqual(b.attack(p),Board.Board.SUNK)

    def testHitAndSinkOneShip(self):
        b = Board.Board(2)
        location = set([Point.Point(0,0), Point.Point(0,1) ])
        b.addShipLocation(location)
        
        self.assertEqual(b.attack(Point.Point(0,0)),Board.Board.HIT)
        self.assertEqual(b.attack(Point.Point(0,1)),Board.Board.SUNK)
    
    def testMissHitAndSinkOneShip(self):
        b = Board.Board(2)
        location = set([Point.Point(0,0), Point.Point(0,1) ])
        b.addShipLocation(location)
        
        self.assertEqual(b.attack(Point.Point(1,1)),Board.Board.MISS)
        self.assertEqual(b.attack(Point.Point(0,0)),Board.Board.HIT)
        self.assertEqual(b.attack(Point.Point(0,1)),Board.Board.SUNK)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSinkOneShip']
    unittest.main()