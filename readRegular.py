from nltk.parse import RecursiveDescentParser
from nltk import CFG, pos_tag, word_tokenize

grammar = CFG.fromstring("""
S -> 'a' S | T
T -> 'b' T | 
""")


rd = RecursiveDescentParser(grammar)

sentence =  list('aaaabbbbb')



for word in sentence:
    correct_grammar=False
    for t in rd.parse(sentence):
        correct_grammar=True

print(correct_grammar)

print(rd)

