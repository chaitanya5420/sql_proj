create schema college;

create table students
(
first_name VARCHAR(30),
last_name VARCHAR(30),
reg_no VARCHAR(10),
dob		VARCHAR(15),
ph_number	INTEGER,
email	VARCHAR(30),
address	VARCHAR(50),
stud_class	VARCHAR(50),
stud_year	INTEGER(5)
);

create table courses
(
course_id int primary key,
course_name varchar(50),
course_books varchar(150),
course_subject varchar(50),
coures_year int
);

CREATE TABLE library (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(100),
    book_subject VARCHAR(100),
    book_class VARCHAR(50),
    book_author VARCHAR(100),
    book_status VARCHAR(20),
    book_publisher VARCHAR(100),
    book_issued_to VARCHAR(100),
    book_count INT,
    book_year INT
);

CREATE TABLE faculty (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(100),
    teacher_qualification VARCHAR(100),
    teacher_degrees VARCHAR(200),
    teacher_speciality VARCHAR(100),
    teacher_certificate VARCHAR(100),
    teacher_class_issued VARCHAR(50),
    teacher_subjects VARCHAR(200),
    teacher_contact VARCHAR(20),
    teacher_email VARCHAR(100),
    teacher_post VARCHAR(100)
);
