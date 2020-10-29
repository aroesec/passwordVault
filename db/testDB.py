import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


con = psycopg2.connect("user=test password='test'");
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

cursor = con.cursor();

name_database = 'test';

sqlcreatedb = "create database "+name_database+";"

cursor.execute(sqlcreatedb);