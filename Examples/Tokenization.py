import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'Brexit is the impending withdrawal of the U.K. from the European Union.')

#for token in doc:
#    print(token.text)


# ----------------------------------------------------------------
# Regular expressions
sentence1 = "Book me a metro from Airport Station to Hong Kong Station."
sentence2 = "Book me a cab to Hong Kong Airport from AsiaWorld-Expo."
import re
from_to = re.compile('.* from (.*) to (.*)')
to_from = re.compile('.* to (.*) from (.*)')

#print("from_to:{} \n to_from:{} \n".format(from_to,to_from))
from_to_match = from_to.match(sentence2)
to_from_match = to_from.match(sentence2)
if from_to_match and from_to_match.groups():
    _from = from_to_match.groups()[0]
    _to = from_to_match.groups()[1]
    print("from_to pattern matched correctly. Printing values\n")
    print("From: {}, To: {}".format(_from, _to))
elif to_from_match and to_from_match.groups():
    _to = to_from_match.groups()[0]
    _from = to_from_match.groups()[1]
    print("to_from pattern matched correctly. Printing values\n")
    print("From: {}, To: {}".format(_from, _to))