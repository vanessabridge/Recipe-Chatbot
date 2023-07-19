import spacy

nlp = spacy.load("en_core_web_sm")

# Example 1
my_string = u"Google has its headquarters in Mountain View, California having a revenue amount to 109.65 billion US dollars"
doc = nlp(my_string)
print("Example 1 \n")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Example 2
my_string = u"Mark Zuckerberg born May 14, 1984 in New York is an American technology entrepreneur and philanthropist best known for co-founding and leading Facebook as its chairman and CEO."
doc = nlp(my_string)
print("\nExample 2 \n")
for ent in doc.ents:
    print(ent.text, ent.label_)


# Example 3 
my_string = u"I usually wake up at 9:00 AM. 90% of my daytime goes in learning new things."
doc = nlp(my_string)
print("\nExample 3 \n")
for ent in doc.ents:
    print(ent.text, ent.label_)

