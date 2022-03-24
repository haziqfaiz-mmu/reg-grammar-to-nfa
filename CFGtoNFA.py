from nltk.parse import RecursiveDescentParser
from nltk import CFG, pos_tag, word_tokenize
string = "S -> 'a' S | T\nT -> 'b' T | $"


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

#print(f"Q = {getState(string)}")

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

#print(f"sigma = {getSigma(string,Q)}")

def getInitialState(string,Q):
    return string[0]
#print("Initial State = "+getInitialState(string))

def getFinalState(string,sigma):
    F =[]
    
    stringcopy = string
    string = string.split("\n")
    #if there is only a single aphabet as transition
    #it is also a final state
    newsigma =[]
    for x in sigma:
        newsigma.append("|"+x)
        newsigma.append(">"+x)
    
    i=0
    stringcopy = stringcopy.split("\n")
    while(i<len(stringcopy)):
        stringcopy[i] = stringcopy[i].replace("'","").replace(" ","")
        stringcopy[i]=stringcopy[i][-2:]
        i=i+1

    i=0
    while(i<len(stringcopy)):
        print(stringcopy[i] in newsigma)
        if (stringcopy[i] in newsigma):
            F.append(string[i][0])
        i=i+1
    
    #print(f"newsigma = {newsigma}")   
    #print(f"stringcopy = {stringcopy}")

            
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

    return F

#getFinalState(string,sigma)
print(f"Final State = {getFinalState(string,sigma)}")

def getDelta(string,Q,sigma):
    delta={}
    string = string.split("\n")
    #sigma = sigma.add("")

    for line in string:
        delta[line[0]]={}
      
    for state in Q:
        for letter in sigma:
            delta[state][letter] = []

    for line in string:
        line = line[5:].replace("'","").replace(" ","").split("|")
        #print(line)

            



    return delta

delta = getDelta(noDollarString,Q,sigma)
print(delta)

