from db.load_csv import loading_csv
from db.queries import institution_name, course_name, least_common, most_common, count_per_district, free_query

user_choice=int(input('''Please, choice one option!
1. Load CSV into DB 
 
2. Search records by institution name 
 
3. Search records by course name 
 
4. Find most/least common course 
 
5. Show course count per district 
 
6. Free SQL query 
 
7. Exit
'''))
while True
    if user_choice == 1:
        print("loading... please wait...")
        loading_csv()
    if user_choice == 2:
        institution = input("Enter institution name: ")
        institution_name(institution)
    if user_choice == 3:
        curse=input("Enter curse name: ")
        course_name(curse)
    if user_choice == 4:
        choice=int(input("for lest common press 1, for most common press 2: "))
        if choice ==1:
            least_common()
        if choice == 2:
            most_common()
    if user_choice == 5:
        count_per_district()
    if user_choice == 6:
        query=input("Enter free SQL Query: ")
        free_query(query)
    if user_choice == 7:
        break