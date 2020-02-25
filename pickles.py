from words import tokenize
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
def load_knn():
    #Open KNN model
    file = open('./models/model_k29.pkl', 'rb')
    knn = pickle.load(file)
    file.close()
    return knn

def load_nb():
    #Open Naive Bayes model
    file = open('./models/nb_model.pkl', 'rb')
    nb = pickle.load(file)
    file.close()
    return nb