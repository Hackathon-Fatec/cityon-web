import pandas as pd
import numpy as np

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

import string

df = pd.read_csv('./olist.csv')
df = df.drop(["review_text", "review_text_tokenized", "polarity", "kfold_rating", "kfold_polarity", "original_index"], axis=1)
df = df[:40000]
df.head()

df["rating"] = np.where(df["rating"] < 3, 0, 1)

df.shape

df.isnull().sum()

df = df.dropna()

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

stop_words = nltk.corpus.stopwords.words('portuguese')

df.info()

tweets = df["review_text_processed"]
tokenization = [word_tokenize(text.lower()) for text in tweets]

lemmatizer = WordNetLemmatizer()

new_tweets = []

for phrase in tokenization:
  new_phrase = ""
  for token in phrase:
    if not str(token) in stop_words and not token in string.punctuation and "@" not in token and "http" not in token and len(token) > 1 and not token.isdigit():
      new_phrase += lemmatizer.lemmatize(str(token)) + " "
  new_tweets.append(new_phrase[:-1])

df["review_text_processed"] = new_tweets

vect_uni_cv = CountVectorizer(ngram_range=(1,1), stop_words=stop_words)
text_vect_uni_cv = vect_uni_cv.fit_transform(df["review_text_processed"])

X_trainUCV, X_testUCV, y_trainUCV, y_testUCV = train_test_split(text_vect_uni_cv, df["rating"], test_size=0.2, random_state=42)
vect_uni_idf = TfidfVectorizer(ngram_range=(1,1), use_idf=True, norm='l2', stop_words=stop_words)
text_vect_uni_idf = vect_uni_idf.fit_transform(df["review_text_processed"])

X_trainUIDF, X_testUIDF, y_trainUIDF, y_testUIDF = train_test_split(text_vect_uni_idf, df["rating"], test_size=0.2, random_state=42)
rfcUCV = RandomForestClassifier()

rfcUCV.fit(X_trainUCV, y_trainUCV)
y_predUCV = rfcUCV.predict(X_testUCV)

acUCV = accuracy_score(y_testUCV, y_predUCV)

print(f'Score Count Vectorizer Random Forest: {acUCV*100:.2f}%')
rfcidf = RandomForestClassifier()

rfcidf.fit(X_trainUIDF, y_trainUIDF)
y_predUIDF = rfcidf.predict(X_testUIDF)

acUIDF = accuracy_score(y_testUIDF, y_predUIDF)

print(f'Score TFIDF Random Forest: {acUIDF*100:.2f}%')

dtrUVC = DecisionTreeClassifier()

dtrUVC.fit(X_trainUCV, y_trainUCV)

acUCV = dtrUVC.score(X_testUCV, y_testUCV)

print(f'Score Count Vectorizer Decision Tree Classifier: {acUCV*100:.2f}%')

dtridf = DecisionTreeClassifier()

dtridf.fit(X_trainUIDF, y_trainUIDF)

acidf = dtridf.score(X_testUCV, y_testUCV)

print(f'Score TFIDF Decision Tree Classifier: {acidf*100:.2f}%')

import joblib

model_filename = 'sentiment_analyser_model.pkl'
joblib.dump(rfcidf, model_filename)

model_filename = 'sentiment_analyser_vect.pkl'
joblib.dump(vect_uni_idf, model_filename)