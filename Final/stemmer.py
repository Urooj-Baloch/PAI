import nltk
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=['jump','jumping','jumps','jumper']
stemmed_words=[stemmer.stem(word) for word in words]
print(stemmed_words)