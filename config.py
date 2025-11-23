import mysql.connector

def connect():
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database= "soldier_courses_db")
    print("Connected, server version: ", cnx.get_server_info())
    cursor = cnx.cursor()
    return cursor