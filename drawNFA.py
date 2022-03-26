from automathon import NFA

## Epsilon Transition is denoted by '' -> Empty string
Q = {'S', 'T'}
sigma = {'a', 'b'}
delta = {
          'S' : {
                  'a' : ['S'],
                  '' : ['T'],
                  'b' : []
                  },
          'T' : {
                  'a' : [],
                  'b' : ['T'],
                   '' : []
                  },
        }
initialState = 'S'
F = {'T','S'}

automata = NFA(Q, sigma, delta, initialState, F)
## This is an example about creating a NFA with the library
automata.view("NFA Visualization2")
print(automata.isValid())   #True