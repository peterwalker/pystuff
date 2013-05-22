'''
Created on May 21, 2013

@author: localdad
'''
from com.pbw import Change

class ChangeCounter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def countChange(self, amount):
        change = Change.Change()
        pennies = int(round(amount*100,0))
        change.quarters =pennies/25
        pennies = pennies%25
        change.nickels = pennies/10      
        pennies = pennies%10
        change.dimes = pennies/5      
        change.pennies = pennies%5
        return change