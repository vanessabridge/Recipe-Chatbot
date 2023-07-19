import spacy

from spacy.lookups import Lookups
lookups = Lookups()

nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")
my_word = "lemmatizing"
print(lemmatizer.lemmatize(nlp(my_word)[0]))

from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer 
porter_stemmer = PorterStemmer() 
snowball_stemmer = SnowballStemmer("english") 
print(porter_stemmer.stem("fastest")) 
print(snowball_stemmer.stem("fastest"))

