import sqlite3

def execute_query(sql: str, group_name) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql, group_name)
        return cur.fetchall()


sql = F"""
SELECT student_name
FROM students
JOIN groups ON students.group_id = groups.group_id  
WHERE groups.group_name = ?;
"""


if __name__ == "__main__":
    
    group_name = input("Введіть назву групи: ")
    print(execute_query(sql, (group_name,)))