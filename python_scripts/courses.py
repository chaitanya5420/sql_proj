import mysql.connector
import csv

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='college'
)
cursor = conn.cursor()

table_name = "courses"

csv_file = "C:\\Users\\chait\\OneDrive\\Documents\\GitHub\\sql_proj\\datafiles\\courses.csv"

# Read data from CSV file and insert into MySQL table

with open(csv_file, 'r') as file:
   
    data = csv.reader(file)
    next(data)                   # Skip header row
    for row in data:
        
        # Construct SQL INSERT statement with parameterized query
       
        sql = "INSERT INTO courses(course_id, course_name, course_books, course_subject, coures_year) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, row)

# Commit changes and close connections
conn.commit()
cursor.close()
conn.close()
