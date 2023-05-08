import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp ("Apple is looking at buying U.K. startup for $1 billion")
nonstopcounter = 0 
stopcounter = 0 

for token in doc:
    print(token.text, token.pos_, token.dep_)
    print(len(doc))
    if token.is_stop == False:
        nonstopcounter += 1
    else:
        stopcounter += 1

lenght = len (doc)

print(f'Number of tokens: {lenght}')
print(f'Number of stop words: {nonstopcounter}, Number of stop counter:{stopcounter}')