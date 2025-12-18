# db_connection.py
import mysql.connector

def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3307,
        database="school"
    )
    return conn
