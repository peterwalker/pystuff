'''
Created on May 23, 2013

@author: localdad
'''
from com.pbw import Node

class Graph(object):
    '''
    classdocs
    '''
    def __init__(self,size):
        '''
        Constructor
        '''
        self.nodes=[]
        while (size>0):
            self.nodes.append(Node.Node())
            size-=1
            
    def addEdge(self,source, dest):
        self.nodes[source].adjacent.append(dest)
        
    def isCyclic(self):
        for i in range(0,len(self.nodes)):
            visited = [False]*len(self.nodes)            
            if (self.isCyclicUtil(i, visited)):
                return True
        return False
    
    def isCyclicUtil(self, nodeIndex, visited):
        if visited[nodeIndex]:
            return True
        # Mark the current node as visited
        visited[nodeIndex] = True
        # Recurse for all the node adjacent to this node
        for i in range(0,len(self.nodes[nodeIndex].adjacent)):
            index = self.nodes[nodeIndex].adjacent[i]       
            return self.isCyclicUtil(index, visited)
        return False