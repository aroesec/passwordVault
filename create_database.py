import psycopg2
import sys
from encryption import hash_me

#Does hash_me store input or does it just get called? Need it to store input

def create_tables():
    con = None
    con = psycopg2.connect("host='localhost' dbname='os.environ(NAME)' user='aroe' password=os.envion(PASSWORD)")   
    cur = con.cursor()
#Create tables below


