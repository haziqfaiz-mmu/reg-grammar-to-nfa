from automathon import NFA

## Epsilon Transition is denoted by '' -> Empty string
Q = {'S','T'}
sigma = {'a', 'b'}
delta = {
          'S' : {
            'a' : ['S'],
            'b' : [],
            '' : ['T']
        },
        'T' : {
            'a' : [],
            'b' : ['T'],
            '' : []
        },
        
        }
initialState = 'S'
F = {'T'}

nfa = NFA(Q, sigma, delta, initialState, F)

## This is an example about creating a NFA with the library
nfa.view("NFA Visualization")
