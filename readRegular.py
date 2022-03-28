from nltk.parse import RecursiveDescentParser
from nltk import CFG

grammar = CFG.fromstring("""
S -> 'a' S | T
T -> 'b' T | 
""")


rd = RecursiveDescentParser(grammar)

sentence =  list('aaaabbbbb')

def readNFA(sentence):
    for word in sentence:
        correct_grammar=False
        for t in rd.parse(sentence):
            correct_grammar=True
    return correct_grammar

print(f"{readNFA(sentence)}")

