import sqlite3

def get_user(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # FIXED: parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchall()