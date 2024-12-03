from sklearn.feature_extraction.text import CountVectorizer

corpus = ["This is the first document.", "This document is the second document.", "And this is the third one."]
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)
print(f"Count Vectorizer Output (as Matrix):\n{X.toarray()}")
print(f"Feature Names (Words): {vectorizer.get_feature_names_out()}")
