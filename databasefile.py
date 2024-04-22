from flask import g
import sqlite3
# Connection of database with app.
# connect the actual database file
def connect_db():
    sql = sqlite3.connect('C:/Users/fullara/Documents/Codes/Project/Food-Tracker-flask/food_log.db')

    # This used to get result as dictionary instead tuples
    sql.row_factory = sqlite3.Row
    return sql

def get_db():

    # It will check the global object to see if sqlite3_db exits in there.
    # If doesn't then it will added it and connect to the database using it and return the result of the connection.
    if not hasattr(g,'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db