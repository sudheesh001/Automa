'''
@author: Mikhail Dubov
'''
import unittest
import TM
import Move
import Symbols

    
eps = Symbols.EPS

class Test(unittest.TestCase):
    '''
    Some test programs for the Turing machine.
    
    1) TM that increments the given binary integer
    2) TM that adds two binary integers (accepts strings in format 'num1+num2')
    '''

    
    def testIncrementer(self):
        '''
        Turing machine that increments a binary integer by 1.
        '''
        
        ################################################################
        ################################################################
        
        incrementer = TM.TuringMachine()
        
        # State 0: Move Right
        incrementer.addTransition((0, '0'), (0, '0', Move.R))
        incrementer.addTransition((0, '1'), (0, '1', Move.R))
        incrementer.addTransition((0, eps), (1, eps, Move.L))
        
        # State 1: Add 1
        incrementer.addTransition((1, '0'), (2, '1', Move.L))
        incrementer.addTransition((1, '1'), (1, '0', Move.L))
        incrementer.addTransition((1, eps), (2, '1', Move.R))
        
        # State 2: HALT
        # TM should not halt 'outside' the string
        incrementer.addTransition((2, eps), (2, eps, Move.R))
        
        ################################################################
        ################################################################
        
        # Simulation (1)
        inputString = '1000'
        print('Input: ' + inputString)
        outputString = incrementer.simulate(inputString)
        print('Output: ' + outputString + '\n')
        
        # Simulation (2)
        inputString = '1011'
        print('Input: ' + inputString)
        outputString = incrementer.simulate(inputString, True)
        print('Output: ' + outputString + '\n')
        
        # Simulation (3)
        inputString = '1111'
        print('Input: ' + inputString)
        outputString = incrementer.simulate(inputString)
        print('Output: ' + outputString + '\n')
        
        # Simulation (4)
        inputString = '0'
        print('Input: ' + inputString)
        outputString = incrementer.simulate(inputString)
        print('Output: ' + outputString + '\n')
        

    def testAdder(self):
        '''
        Turing machine that adds two binary integers.
        Accepts strings in format 'num1+num2'.
        '''
        
        ################################################################
        ################################################################
        adder = TM.TuringMachine()
        
        # State 0
        adder.addTransition((0, eps), (1, eps, Move.L))
        adder.addTransition((0, '0'), (0, '0', Move.R))
        adder.addTransition((0, '1'), (0, '1', Move.R))
        adder.addTransition((0, 'a'), (0, 'a', Move.R))
        adder.addTransition((0, 'b'), (0, 'b', Move.R))
        adder.addTransition((0, '+'), (0, '+', Move.R))
        
        # State 1
        adder.addTransition((1, '0'), (2, eps, Move.L))
        adder.addTransition((1, '1'), (3, eps, Move.L))
        adder.addTransition((1, '+'), (2, eps, Move.L))
        
        # State 2
        adder.addTransition((2, eps), (7, eps, Move.R))
        adder.addTransition((2, '0'), (2, '0', Move.L))
        adder.addTransition((2, '1'), (2, '1', Move.L))
        adder.addTransition((2, 'a'), (2, '0', Move.L))
        adder.addTransition((2, 'b'), (2, '1', Move.L))
        adder.addTransition((2, '+'), (4, '+', Move.L))
        
        # State 3
        adder.addTransition((3, '0'), (3, '0', Move.L))
        adder.addTransition((3, '1'), (3, '1', Move.L))
        adder.addTransition((3, '+'), (5, '+', Move.L))
        
        # State 4
        adder.addTransition((4, eps), (0, 'a', Move.R))
        adder.addTransition((4, '0'), (0, 'a', Move.R))
        adder.addTransition((4, '1'), (0, 'b', Move.R))
        adder.addTransition((4, 'a'), (4, 'a', Move.L))
        adder.addTransition((4, 'b'), (4, 'b', Move.L))
        
        # State 5
        adder.addTransition((5, eps), (0, 'b', Move.R))
        adder.addTransition((5, '0'), (0, 'b', Move.R))
        adder.addTransition((5, '1'), (6, 'a', Move.L))
        adder.addTransition((5, 'a'), (5, 'a', Move.L))
        adder.addTransition((5, 'b'), (5, 'b', Move.L))
        
        # State 6
        adder.addTransition((6, eps), (0, '1', Move.R))
        adder.addTransition((6, '0'), (0, '1', Move.R))
        adder.addTransition((6, '1'), (6, '0', Move.L))
        
        # State 7 - HALT
        
        ################################################################
        ################################################################
        
        # Simulation (1)
        inputString = '111+1001'
        print('Input: ' + inputString)
        outputString = adder.simulate(inputString, True)
        print('Output: ' + outputString + '\n')
        
        # Simulation (2)
        inputString = '111+11'
        print('Input: ' + inputString)
        outputString = adder.simulate(inputString)
        print('Output: ' + outputString + '\n')
        
        # Simulation (3)
        inputString = '111+0'
        print('Input: ' + inputString)
        outputString = adder.simulate(inputString)
        print('Output: ' + outputString + '\n')
        
        # Simulation (4)
        inputString = '100+1'
        print('Input: ' + inputString)
        outputString = adder.simulate(inputString)
        print('Output: ' + outputString + '\n')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()