import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT AVG(rating) AS average_rating
FROM magazine;
"""


if __name__ == "__main__":
    print(execute_query(sql))