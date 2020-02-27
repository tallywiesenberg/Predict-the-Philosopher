import pickle

def load_2d_vectors():
    '''Load PCA 2d document vectors from Pickle file'''
    array = open('./models/word_vectors.pkl', 'rb')
    return pickle.load(array)

def tokenize(doc):
    '''Tokenizer with lemmatizer'''
    return [token.lemma_ for token in nlp(doc) if (token.is_stop == False) &
            (token.is_punct == False) & (token.is_space == False) &
            (token.is_upper == False) & (token.pos_ != 'PROPN')]
