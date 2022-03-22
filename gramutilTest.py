from gramutil import cfg

grammarString = """S -> a S | T
T -> b T | """
grammarString2 = "S -> a S | $ "
grammar = cfg.ContextFreeGrammar(grammarString2)

pda = grammar.toPDA()

#print(grammar)
#print(pda)
pdaString = str(pda)

print(pdaString)
