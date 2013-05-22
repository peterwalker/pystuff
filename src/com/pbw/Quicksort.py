'''
Created on May 22, 2013

@author: localdad
'''

class Quicksort(object):
    '''
    classdocs
    '''
    ordered=[]

    def __init__(self):
        '''
        Constructor
        '''
    def sort(self, unsorted):
        self.ordered = unsorted
        if (len(self.ordered) == 0):
            return self.ordered
        self.partition(0,len(self.ordered)-1)
        return self.ordered
    
    def partition(self, low, high):
        i = low
        j = high
        # Get the pivot element from the middle of the list
        pivot = self.ordered[low + (high - low) / 2];

        # Divide into two lists
        while (i <= j): 
            # If the current value from the left list is smaller then the pivot
            # element then get the next element from the left list
            while (self.ordered[i] < pivot) :
                i+=1
            # If the current value from the right list is larger then the pivot
            # element then get the next element from the right list
            while (self.ordered[j] > pivot) :
                j-=1
            
            # If we have found a values in the left list which is larger then
            # the pivot element and if we have found a value in the right list
            # which is smaller then the pivot element then we exchange the
            # values.
            # As we are done we can increase i and decrease j
            if (i <= j):
                self.swap(i, j)
                i+=1
                j-=1
            
        # Recurse left of the pivot
        if (low < j):
            self.partition(low, j)
        # Recurse right of the pivot
        if (i < high):
            self.partition(i, high)
    
    def swap(self,i,j): 
        temp = self.ordered[i]
        self.ordered[i] = self.ordered[j]
        self.ordered[j] = temp