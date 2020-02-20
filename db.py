from decouple import config
import pickle
import pandas
import psycopg2
import sqlalchemy

#Load Pandas CSV from Pickle file
def load_data():
    df = pickle.load(open('./data/dataframe.pkl', 'rb'))
    return df
#Import pandas CSV into Extracts table
def populate_table():
    '''Create and populate postgreSQL table "extracts" and populate with pandas dataframe'''

    #Credentials
    db = 'vsodlxyb'
    user = 'vsodlxyb'
    password = config('DB_PASSWORD')
    host = 'rajje.db.elephantsql.com'

    #Connect to database
    conn = psycopg2.connect(
        dbname=db,
        user=user,
        password=password,
        host=host
    )
    curs = conn.cursor()
    
    #Create Table
    curs.execute('''
    CREATE TABLE IF NOT EXISTS extracts(
        id serial PRIMARY KEY,
        extract TEXT,
        author VARCHAR(8)
    )
    ''')
    conn.close()
    
    #Populate table "extracts"
    engine = sqlalchemy.create_engine('postgres://vsodlxyb:j8-RAO4oL8UbZVlwxuwy6qX7zg_2teoG@rajje.db.elephantsql.com:5432/vsodlxyb')
    con = engine.connect()
    table_name = 'extracts'
    df = load_data()
    df.to_sql(table_name, con)
    con.close()