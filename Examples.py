import spacy
nlp = spacy.load("en_core_web_sm")

print('Example 1: \n')
# Example: 1
doc = nlp(u'I am learning how to build chatbots') #Creates a doc object
for token in doc:
    print(token.text, token.pos_) #prints the text and POS

print('\n Example 2: \n')
# Example 2
doc = nlp(u'Iam going to London nexr week for a meeting')
for token in doc:
    print(token.text, token.pos_) 

print('\n Example 3: \n')

doc = nlp(u'Google release "Move Mirror" AI experiemnt that matches your pose from 80,000 images')

for token in doc:
    print(token.text,token.lemma, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)