'''
Created on May 23, 2013

@author: localdad
'''
import unittest
from com.pbw import Graph

class DetectCycleTest(unittest.TestCase):

    def testNoCycle(self):
        g = Graph.Graph(3)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        self.assertFalse(g.isCyclic())
        
    def testSelfReferenceCycle(self):
        g = Graph.Graph(2)
        g.addEdge(0, 1)
        g.addEdge(1, 1)
        self.assertTrue(g.isCyclic())        

    def testSimpleCycle(self):
        g = Graph.Graph(2)
        g.addEdge(0, 1)
        g.addEdge(1, 0)
        self.assertTrue(g.isCyclic())       
         
    def testCycles(self):
        g = Graph.Graph(4)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)
        self.assertTrue(g.isCyclic()) 
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNoCycle']
    unittest.main()