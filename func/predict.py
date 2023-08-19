import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import string

lemmatizer = WordNetLemmatizer()
def predict(opinion):
    model_filename = "../models/sentiment_analyser_model.pkl"
    vect_filename = "../models/sentiment_analyser_vect.pkl"

    loaded_model = joblib.load(model_filename)
    loaded_vectorizer = joblib.load(vect_filename)

    stop_words = nltk.corpus.stopwords.words('portuguese')

    new_data = word_tokenize(opinion.lower())
    new_opinion = " ".join([lemmatizer.lemmatize(str(token)) for token in new_data if not str(token) in stop_words and not token in string.punctuation and "@" not in token and "http" not in token and len(token) > 1 and not token.isdigit()])

    new_data_transformed = loaded_vectorizer.transform([new_opinion])
    predictions = loaded_model.predict(new_data_transformed)
    
    return "Positive" if predictions[0] == 1 else "Negative"