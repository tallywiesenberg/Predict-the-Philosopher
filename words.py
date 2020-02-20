import pickle
import spacy

#Load spacy model
nlp = spacy.load("en_core_web_lg")

def get_doc_vectors(words):
    #Converts a doc into a vector
    return nlp(words).vector

def load_2d_vectors():
    '''Load PCA 2d document vectors from Pickle file'''
    array = open('./models/word_vectors.pkl', 'rb')
    return pickle.load(array)
