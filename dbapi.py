############------------ IMPORTS ------------############
import sqlite3
from sqlite3.dbapi2 import connect


############------------ GLOBAL VARIABLE(S) ------------############
conn =  sqlite3.connect("Cookies")

cursor = conn.cursor()


############------------ FUNCTION(S) ------------############
cursor.execute(
    "select host_key from cookies limit 10")

results = cursor.fetchall()

print(results)
conn.close()

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass