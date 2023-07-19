from spacy.lang.en.stop_words import STOP_WORDS
import spacy

nlp = spacy.load("en_core_web_sm")

print(STOP_WORDS)
print(len(STOP_WORDS))
print("Check if Stop word? \n")
print("is: ",nlp.vocab[u'is'].is_stop)
print("hello: ",nlp.vocab[u'hello'].is_stop)
print("with: ",nlp.vocab[u'with'].is_stop)