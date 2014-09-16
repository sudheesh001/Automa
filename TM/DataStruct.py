'''
@author: Mikhail Dubov
'''
import Move
import Symbols

class Zipper:
    '''
    Zipper data structure implementation.
    Serves as the Turing machine strip.
    '''

    def __init__(self, string=''):
        ''' Constructor '''
        self.l = Symbols.EPS
        self.r = string + Symbols.EPS
        
    
    def read(self):
        ''' Reads the symbol under the tape head '''
        return self.r[0]
    
    
    def write(self, symbol):
        ''' Writes the symbol onto the strip under the tape head '''
        self.r = symbol + self.r[1:]
        # Preserve epsilons at the edges
        if (symbol <> Symbols.EPS):
            if (len(self.l) == 0):
                self.l = Symbols.EPS
            elif (len(self.r) == 1):
                self.r += Symbols.EPS
        
    
    def move(self, direction):
        ''' Moves the tape head in the given direction '''
        if (direction == Move.R):
            if (len(self.r) == 0):
                self.l = Symbols.EPS + self.l
            else:
                self.l = self.r[0] + self.l
                self.r = self.r[1:]
        else:
            if (len(self.l) == 0):
                self.r = Symbols.EPS + self.r
            else:
                self.r = self.l[0] + self.r
                self.l = self.l[1:]
            
            
    def left(self):
        ''' Returns part of the word on the left side of the tape head '''
        # S[::-1] reverses the string (!)
        res = self.l[::-1]
        # Delete epsilons at the edges 
        while(len(res) > 0 and res[0] == Symbols.EPS):
            res = res[1:]
        return res
    
    
    def right(self):
        '''
        Returns part of the word on the right side of the tape head,
        including the symbol under the tape head
        '''
        res = self.r[:] # Make a copy
        # Delete epsilons at the edges 
        while(len(res) > 0 and res[-1] == Symbols.EPS):
            res = res[:-1]
        return res
    
    
    def string(self):
        ''' Returns the word on the strip '''
        return self.left() + self.right()
        
        
    def __str__(self):
        return self.string()
        