import csv
import mysql.connector



def loading_csv():
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1", database= "soldier_courses_db")
    print("Connected, server version: ", cnx.get_server_info())
    cursor = cnx.cursor()
    with open("./data/courses.csv", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute("INSERT INTO courses (institution, city, address, course, district, telephone, email) VALUES (%s, %s, %s, %s, %s, %s, %s);",row)

        cnx.commit()
    # cursor.close()
    # cnx.close()


