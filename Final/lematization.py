from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
words = ["running", "ran", "better", "best"]

# Lemmatization based on Part of Speech
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
print(f"Lemmatized Words (Verb): {lemmatized_words}")
