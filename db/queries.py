from config import connect

def institution_name(institution):
    cnx=connect()
    cursor=cnx.cursor()
    cursor.execute(f"SELECT * FROM courses WHERE institution LIKE '%{institution}%' LIMIT 50;")
    data=cursor.fetchall()
    print(data)
def course_name(course):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT * FROM courses WHERE course LIKE '%{course}%' LIMIT 50;")
    data = cursor.fetchall()
    print(data)
def most_common():
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT course, COUNT(*) AS num FROM courses GROUP BY course ORDER BY num DESC LIMIT 1;")
    data = cursor.fetchall()
    print(data)
def least_common():
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT course, COUNT(*) AS num FROM courses GROUP BY course ORDER BY num ASC LIMIT 1;")
    data = cursor.fetchall()
    print(data)
def count_per_district():
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT district, COUNT(*) AS num_courses FROM courses GROUP BY district ORDER BY num_courses DESC;")
    data = cursor.fetchall()
    print(data)
def free_query(query):
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)