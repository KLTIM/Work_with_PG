
import psycopg2	as pg
from config import *
from CreateTable import *

try:
    connection = pg.connect(host=host,
                  port=port,
                  dbname=dbname,
                  user=user,
                  password=password)
    connection.autocommit=True
    createOwnersTable(connection.cursor())
    createUsersTable(connection.cursor())
    createUrlTable(connection.cursor())
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL: ", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")