import sqlite3

def execute_query(sql: str, subject_name: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, (subject_name,))
        return cur.fetchone()  # Використовуємо fetchone()

sql = f"""
SELECT student_name, AVG(rating) AS average_rating
FROM students
JOIN magazine ON students.student_id = magazine.student_id
JOIN subjects ON magazine.subject_id = subjects.subject_id 
WHERE subjects.subject_name = ?
GROUP BY student_name
ORDER BY average_rating DESC
LIMIT 1;
"""

if __name__ == "__main__":
    subject_name = input("Введіть назву предмету: ")
    print(execute_query(sql, subject_name))