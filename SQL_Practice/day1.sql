
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
);

INSERT INTO students (student_id, name, age, city)
VALUES (1, 'Rohit', 21, 'Pune');

SELECT * FROM students;

