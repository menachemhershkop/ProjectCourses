from db.load_csv import loading_csv
from db.queries import queiries

user_choice=int(input('''Please, choice one option!
1. Load CSV into DB 
 
2. Search records by institution name 
 
3. Search records by course name 
 
4. Find most/least common course 
 
5. Show course count per district 
 
6. Free SQL query 
 
7. Exit
'''))

if user_choice == 1:
    print("loading... please wait...")
    loading_csv()
if user_choice == 2:
    querie= input("Enter your quire: ")
    queiries(querie)
if user_choice == 3:
    pass
if user_choice == 4:
    pass
if user_choice == 5:
    pass
if user_choice == 6:
    pass
if user_choice == 7:
    pass