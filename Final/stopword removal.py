from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

text = "This is a simple sentence with some stopwords."
words = word_tokenize(text)

filtered_words = [word for word in words if word.lower() not in stop_words]
print(f"Filtered Words: {filtered_words}")
