from decouple import config
import pickle
import pandas
import psycopg2
import sqlalchemy

#Load Pandas CSV from Pickle file
def load_data():
    df = pickle.load(open('./data/dataframe.pkl', 'rb'))
    return df