from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

texts = ["I love data", "Data is fun"]

# Bag of Words
bow = CountVectorizer()
print("BoW Matrix:\n", bow.fit_transform(texts).toarray())

# TF-IDF
tfidf = TfidfVectorizer()
print("TF-IDF Matrix:\n", tfidf.fit_transform(texts).toarray())
