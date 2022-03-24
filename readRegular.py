from nltk.parse import RecursiveDescentParser
from nltk import CFG, pos_tag, word_tokenize


grammar = CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> 'the' N | N PP | 'the' N PP
 VP -> V NP | V PP | V NP PP
 N -> 'cat'
 N -> 'dog'
 N -> 'rug'
 V -> 'chased'
 V -> 'sat'
 P -> 'in'
 P -> 'on'
 """)

grammar2 = CFG.fromstring("""
S -> 'a' S | T
T -> 'b' T | 
""")


rd = RecursiveDescentParser(grammar)
rd2 = RecursiveDescentParser(grammar2)

string2 = "S -> 'a' S | T\nT -> 'b' T | "
grammar3 = CFG.fromstring(string2)
rd3 = RecursiveDescentParser(grammar3)

sentence1 = 'the cat chased the dog'.split()
sentence2 = 'the cat chased the dog on the rug'.split()
sentence3 =  list('aaaabbbbb')

#for t in rd.parse(sentence1):
#     print(t)

#for t in rd2.parse(sentence3):
#    print(t)

for word in sentence3:
    correct_grammar=False
    for t in rd3.parse(sentence3):
        correct_grammar=True

print(correct_grammar)

print(rd3)

