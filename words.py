import pickle
import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

def load_2d_vectors():
    '''Load PCA 2d document vectors from Pickle file'''
    array = open('./models/word_vectors.pkl', 'rb')
    return pickle.load(array)

def get_doc_vectors(words):
    # converts a list of words into their word vectors
    return nlp(words).vector
