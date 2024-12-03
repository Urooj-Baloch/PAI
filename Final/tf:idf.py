from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["This is the first document.", "This document is the second document.", "And this is the third one."]
tfidf_vectorizer = TfidfVectorizer()

X_tfidf = tfidf_vectorizer.fit_transform(corpus)
print(f"TF-IDF Output (as Matrix):\n{X_tfidf.toarray()}")
print(f"Feature Names (Words): {tfidf_vectorizer.get_feature_names_out()}")
