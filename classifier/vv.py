import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

X_train = ["fake news example", "real news example"]
y_train = [0, 1]  # 0 = fake, 1 = real

vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_vectors, y_train)

with open('classifier/classifier_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)
