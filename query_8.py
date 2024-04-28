import sqlite3

def execute_query(sql: str, teacher_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, teacher_name)
        return cur.fetchall()

sql = f"""
SELECT AVG(magazine.rating) AS average_rating
FROM magazine
JOIN subjects ON magazine.subject_id = subjects.subject_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.teacher_name = ?;
"""

if __name__ == "__main__":
    teacher_name = input("Введіть ім'я викладача: ")
    print(execute_query(sql, (teacher_name,)))