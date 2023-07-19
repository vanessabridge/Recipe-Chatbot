import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'Book me a flight from Bangalore to Goa')
blr, goa = doc[5], doc[7]
print(list(blr.ancestors)) 
print(list(goa.ancestors))
print(list(doc[4].ancestors))
doc[3].is_ancestor(doc[5])

# Example 2
print("\n Ancestors \n")
doc = nlp(u'Book a table at the restaurant and the taxi to the hotel')
tasks = doc[2], doc[8] #(table, taxi)
tasks_target = doc[5], doc[11] #(restaurant, hotel)

for task in tasks_target:
    for tok in task.ancestors:
        if tok in tasks:
            print("Booking of {} belongs to {}".format(tok,task))
    break

print("\nChildren \n")
print(list(doc[3].children))

# Example: Dependency Parsing
doc = nlp(u'Book a table at the restaurant and the taxi to the hotel')
#displacy.serve(doc, style='dep')

# Example of Dependency Parsing

doc1 = nlp(u"What are some places to visit in Berlin and stay in Lubeck")
places = [doc1[7], doc1[11]] # Berlin, Lubeck
actions = [doc1[5],doc1[9]]

for place in places:
    for tok in place.ancestors:
        if tok in actions:
            print("User is referring {} to {}".format(place, tok))
            break

print("\nNOUN CHUNKS\n")
doc = nlp(u"Boston Dynamics is gearing up to produce thousands of robot dogs")
print(list(doc.noun_chunks))

doc = nlp(u"Deep learning cracks the code of messenger RNAs and protein-coding potential")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)
print("\n\n")    
# Tokenized

doc = nlp(u'How are you doing today?')
for token in doc:
    print(token.text, token.vector[:5])

print("\n\n") 
# Examples of Similarities, needs differernt model (ie: not en_core_web_sm)
nlp = spacy.load("en_core_web_lg")
hello_doc = nlp(u"hello")
hi_doc = nlp(u"hi")
hella_doc = nlp(u"hella")
print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))
print("\n\n") 
example_doc = nlp(u"car truck google")
for t1 in example_doc:
    for t2 in example_doc:
        similarity_perc = int(t1.similarity(t2) * 100)
        print ("Word {} is {}% similar to word {}".format(t1.text,similarity_perc,  t2.text))