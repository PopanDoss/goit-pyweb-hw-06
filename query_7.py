import sqlite3

def execute_query(sql: str, params) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, params)
        return cur.fetchall()

sql = f"""
SELECT students.student_name, magazine.rating
FROM students
JOIN groups ON students.group_id = groups.group_id
JOIN magazine ON students.student_id = magazine.student_id
JOIN subjects ON magazine.subject_id = subjects.subject_id
WHERE groups.group_name = ? AND subjects.subject_name = ?;
"""

if __name__ == "__main__":
    group_name = input("Введіть назву групи: ")
    subject_name = input("Введіть назву предмету: ")
    print(execute_query(sql, (group_name, subject_name)))