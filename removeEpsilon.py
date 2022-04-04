sigma = {'a', 'b'}
Q = {'S','T'}
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

def removeEpsilon(Q,delta,sigma):
    for state in Q:
        if(delta[state]['']):
            print(delta[state])
            epsilonset = set(delta[state][''])
            for letter in sigma:
                templist=set(delta[state][letter])
                templist = list(templist | epsilonset)
                delta[state][letter] = templist
    for state in Q:
        delta[state].pop('')
    return delta

print(removeEpsilon(Q,delta,sigma))

