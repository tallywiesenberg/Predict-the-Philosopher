import pickle
import spacy

#Load spacy model
nlp = spacy.load("en_core_web_lg")

def get_doc_vectors(words):
    # converts a list of words into their word vectors
    tokens = tokenize(words)
    string = ' '.join(tokens)
    return nlp(string).vector

def load_2d_vectors():
    '''Load PCA 2d document vectors from Pickle file'''
    array = open('./models/word_vectors.pkl', 'rb')
    return pickle.load(array)

def tokenize(doc):
    '''Tokenizer with lemmatizer'''
    return [token.lemma_ for token in nlp(doc) if (token.is_stop == False) &
            (token.is_punct == False) & (token.is_space == False) &
            (token.is_upper == False) & (token.pos_ != 'PROPN')]
