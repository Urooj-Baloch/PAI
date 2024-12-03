import nltk
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize
text='This is simple program.hope,it will run'
words=word_tokenize(text)
print(words)
sen=sent_tokenize(text)
print(sen)