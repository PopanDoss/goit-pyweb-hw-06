import sqlite3
import sys

def execute_query(sql: str, subject_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, subject_name)
        return cur.fetchall()


sql = f"""
SELECT g.group_name, AVG(m.rating) AS average_rating
FROM groups g
JOIN students s ON g.group_id = s.group_id
JOIN magazine m ON s.student_id = m.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
WHERE sub.subject_name = ?
GROUP BY g.group_name;
"""

if __name__ == "__main__":
    subject_name = input("Введіть назву предмету :", )
    print(execute_query(sql, (subject_name,)))