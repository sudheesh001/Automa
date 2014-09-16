'''
@author: Mikhail Dubov
'''
import DataStruct

class TuringMachine:
    '''
    Turing Machine implementation.
    
    Accepts by halting.
    Start state is numbered 0.
    '''


    def __init__(self):
        ''' Constructor '''
        self.program = []
        self.strip = DataStruct.Zipper()
        self.state = 0
        
        
    def addTransition(self, (state1, symbol1), (state2, symbol2, direction)):
        ''' Adds a transition rule to the Turing machine transition function '''
        while (state1 >= len(self.program)):
            self.program.append({}) # self.program is a list of Dictionaries
        self.program[state1][symbol1] = (state2, symbol2, direction)
        
        
    def IDstring(self):
        ''' Returns a string that indicates the current ID of the Turing machine '''
        return self.strip.left() + '[q' + str(self.state) + ']' + self.strip.right()
        
        
    def simulate(self, string, trace=False):
        '''
        Simulates the current Turing machine on given input,
        returns the corresponding output. The second optional
        parameter, if set to True, enables tracing of
        Turing machine steps in the console (False by default).
        '''
        
        self.strip = DataStruct.Zipper(string)
        self.state = 0
        
        halt = False
        
        while(not halt):
            symbol = self.strip.read()
            
            if (trace):
                print(self.IDstring())
            
            # self.program[self.state] is a Dictionary
            if (self.state < len(self.program) and
                symbol in self.program[self.state]):
                # Perform 1 step
                (q, S, D) = self.program[self.state][symbol]
                self.strip.write(S)
                self.strip.move(D)
                self.state = q
            else:
                halt = True
                
        return self.strip.string()
            
            