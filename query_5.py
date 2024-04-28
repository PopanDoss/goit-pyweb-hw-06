import sqlite3

def execute_query(sql: str, teacher_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, teacher_name)
        return cur.fetchall()


sql = F"""
SELECT subject_name
FROM subjects
WHERE teacher_id = (SELECT teacher_id FROM teachers WHERE teacher_name = ?);
"""


if __name__ == "__main__":
    
    teacher_name = input("Введіть ім'я викладача: ")
    print(execute_query(sql, (teacher_name,)))