import sqlite3

def execute_query(sql: str, student_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, student_name)
        return cur.fetchall()

sql = f"""
SELECT DISTINCT subjects.subject_name
FROM subjects
JOIN magazine ON subjects.subject_id = magazine.subject_id
JOIN students ON magazine.student_id = students.student_id
WHERE students.student_name = ?;
"""

if __name__ == "__main__":
    student_name = input("Введіть ім'я студента: ")
    print(execute_query(sql, (student_name,)))