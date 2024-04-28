import sqlite3

def execute_query(sql: str, student_teacher_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, student_teacher_name)
        return cur.fetchall()

sql = f"""
SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN magazine ON subjects.subject_id = magazine.subject_id
JOIN students ON magazine.student_id = students.student_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE students.student_name = ? AND teachers.teacher_name = ?;
"""

if __name__ == "__main__":
    student_name = input("Введіть ім'я студента: ")
    teacher_name = input("Введіть ім'я викладача: ")
    print(execute_query(sql, (student_name, teacher_name)))