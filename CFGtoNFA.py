from nltk.parse import RecursiveDescentParser
from nltk import CFG

string = """S -> 'a' S | T
        T -> 'b'"""


noDollarString = string.replace('$','')
grammar = CFG.fromstring(noDollarString)
#print(grammar)

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

def getState(string):
    Q=[]
    Q.append(string[0])
    i=0
    while( i < len(string)):
        if (string[i]=="\n"):
            Q.append(string[i+1])
        i=i+1
    Q = set(Q)
    return Q

print(f"Q = {getState(string)}")

def getSigma(string,Q):
    sigma=[]
    nonSigma = [' ', '-', '>', '|', "\n", "'","$"]
    for word in Q:
        nonSigma.append(word)
    for word in string:
        if (word not in nonSigma) and(word not in sigma):
            sigma.append(word)
    sigma = set(sigma)
    return sigma

print(f"sigma = {getSigma(string,Q)}")

def getInitialState(string,Q):
    return string[0]
print("Initial State = "+getInitialState(string,Q))


def buildStateDict(sigma,newState,delta):
    delta[newState]={}
    for letter in sigma:
        delta[newState][letter] = []
    return delta[newState]

def getFinalState(string,sigma,Q,delta):
    F =[]
    
    string = string.replace("\t","").replace(" ","")
    stringcopy = string
    string = string.split("\n")
    #if there is only a single aphabet as transition
    #it must lead to a new final state
    # add new state into Q,F and delta 
    newsigma =[]
    for x in sigma:
        newsigma.append("|"+x)
        newsigma.append(">"+x)
    
    i=0
    stringcopy = stringcopy.split("\n")
    while(i<len(stringcopy)):
        stringcopy[i] = stringcopy[i].replace("'","").replace(" ","")
        stringcopy[i]=stringcopy[i][0]+stringcopy[i][3]+stringcopy[i][-2:]
        print("stringcopy = " +stringcopy[i])
        i=i+1

    i=0
    while(i<len(stringcopy)):
        #print(stringcopy[i] in newsigma)
        if (stringcopy[i][-2:] in newsigma):
            F.append("New State")
            Q.add("New State")
            delta["New State"] = buildStateDict(sigma,"New State",delta)
            delta[stringcopy[i][0]][stringcopy[i][1]].append("New State")

        print("string[i] = "+string[i])
        i=i+1
    
    #if there is epsilon it must be a final state
    i=0
    while(i<len(string)):
        if(string[i].find("$")!=-1):
            F.append(string[i][0])
        i=i+1

    #if you can go directly to the final state from
    #another state, then it is also a final state
    Fcopy=F
    i=0
    for word in Fcopy:
        #word = " "+word
        while(i<len(string)):
            if(string[i].find(word)!=-1):
                if(string[i][0] not in F):
                    F.append(string[i][0])  
            i=i+1 

    return [Q,F,delta]

print(f"Final State = {getFinalState(string,sigma,Q,delta)}")


def getDelta(string,Q,sigma):
    delta={}
    sigma.add(" ")
    
    #built the dictionary
    for state in Q:
        delta[state]={}
        for letter in sigma:
            delta[state][letter] = []

    string = string.replace(" ","").replace("'","")
    
    #find epsilon transition function
    string = string.split("\n")
    
    for line in string:
        i=0
        while(i<len(line)-1):
            if (line[i] in sigma and line[i+1] in Q):
                delta[line[0]][line[i]].append(line[i+1])
            if(line[i] in Q and line[i-1] not in sigma and i!=0):
                delta[line[0]][" "].append(line[i])
            i=i+1



    #print(string)
    return delta

delta = getDelta(string,Q,sigma)
print(f"delta = {delta}")

