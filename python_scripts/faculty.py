import mysql.connector
import csv

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    database='college'
)
cursor = conn.cursor()

table_name = "faculty"

csv_file = "C:\\Users\\chait\\OneDrive\\Documents\\GitHub\\sql_proj\\datafiles\\faculty.csv"

# Read data from CSV file and insert into MySQL table
with open(csv_file, 'r') as file:
    data = csv.reader(file)
    next(data)  # Skip header row
    for row in data:
      
        # Construct SQL INSERT statement with parameterized query
      
        sql = "INSERT INTO faculty (teacher_id,	teacher_name, teacher_qualification, teacher_degrees, teacher_speciality, teacher_certificate, teacher_class_issued, teacher_subjects,	teacher_contact, teacher_email,	teacher_post) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, row)

# Commit changes and close connections
conn.commit()
cursor.close()
conn.close()
