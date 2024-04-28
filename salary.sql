-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(255) NOT NULL
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name VARCHAR(255) NOT NULL
    
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name VARCHAR(255) NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Table: magazine
DROP TABLE IF EXISTS magazine;
CREATE TABLE magazine (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER,
    student_id INTEGER,
    rating INTEGER ,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);