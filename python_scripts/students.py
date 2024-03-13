import mysql.connector
import csv

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='college'
)
cursor = conn.cursor()

table_name = "students"

csv_file = "C:\\Users\\chait\\OneDrive\\Documents\\GitHub\\sql_proj\\datafiles\\students.csv"

# Read data from CSV file and insert into MySQL table
with open(csv_file, 'r') as file:
    data = csv.reader(file)
    next(data)  # Skip header row
    for row in data:
        
        # Construct SQL INSERT statement with parameterized query
        
        sql = "INSERT INTO students (first_name, last_name, dob, email, ph_number, reg_no, address, stud_class, stud_year) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, row)

# Commit changes and close connections
conn.commit()
cursor.close()
conn.close()
