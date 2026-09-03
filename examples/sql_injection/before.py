import sqlite3

def get_user(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # VULNERABLE: string concatenation allows SQL injection
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchall()