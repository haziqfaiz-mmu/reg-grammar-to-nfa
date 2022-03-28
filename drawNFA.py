from automathon import NFA

## Epsilon Transition is denoted by '' -> Empty string
Q = {'q1', 'q2', 'q3', 'q4'}
sigma = {'0', '1'}
delta = {
          'q1' : {
                  '0' : ['q1'],
                  '1' : ['q1', 'q2']
                  },
          'q2' : {
                  '0' : ['q3'],
                  '' : ['q3']
                  },
          'q3' : {
                  '1' : ['q4'],
                  },
          'q4' : {
                  '0' : ['q4'],
                  '1' : ['q4'],
                  },
        }
initialState = 'q1'
F = {'q4'}

nfa = NFA(Q, sigma, delta, initialState, F)
noepsilon = nfa.removeEpsilonTransitions()
dfa = nfa.getDFA()
## This is an example about creating a NFA with the library
nfa.view("NFA Visualization")
noepsilon.view("No Epsilon NFA")
dfa.view("DFA")