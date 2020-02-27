from decouple import config
import pickle
import pandas as pd
import psycopg2
import sqlalchemy

#Load Pandas CSV from Pickle file
def load_data():
    df = pd.read_csv('./data/dataframe.csv')
    return df