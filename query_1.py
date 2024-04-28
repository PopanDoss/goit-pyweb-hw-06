import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT student_name, AVG(rating) AS average_rating
FROM students
JOIN magazine ON students.student_id = magazine.student_id
GROUP BY student_name
ORDER BY average_rating DESC
LIMIT 5;
"""


if __name__ == "__main__":
    print(execute_query(sql))