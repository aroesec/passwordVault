import psycopg2 ##module won't import
import sys
from encryption import hash_me

#Does hash_me store input or does it just get called? Need it to store input

user = input('Please enter a username to store into the databse')

hash_me() ##gives password from the encryption file

def create_tables():
    conn = psycopg2.connect("host='localhost' dbname='os.environ(NAME)' user='aroe' password=os.envion(PASSWORD)")
       
    cur = con.cursor()
    cur.execute("CREATE TABLE users (id serial PRIMARY KEY, num integer, data varchar);")
    cur.execute(f"INSERT INTO users({user}, {password}) VALUES(%s, %s")



def queryTable():
    ##example query below
    cure.execute('SELECT * FROM users;') ##in-line query
    cur.fetchone()

    ##user and password variables need to be input in CLI
#Create tables below


