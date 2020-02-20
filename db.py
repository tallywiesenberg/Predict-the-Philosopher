from decouple import config
import psycopg2

db = 'vsodlxyb'
user = 'vsodlxyb'
password = config('DB_PASSWORD')
host = 'rajje.db.elephantsql.com'

conn = psycopg2.connect(
    dbname=db,
    user=user,
    password=password,
    host=host
)