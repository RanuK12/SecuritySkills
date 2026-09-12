from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('app.db')
    return conn

@app.route('/store', methods=['POST'])
def store():
    user_input = request.form['input']
    conn = get_db()
    # Assume storage is safe (we are using parameterized query here for storage)
    conn.execute("INSERT INTO storage (data) VALUES (?)", (user_input,))
    conn.commit()
    conn.close()
    return 'Stored'

@app.route('/use')
def use():
    conn = get_db()
    # Retrieve the stored data
    row = conn.execute("SELECT data FROM storage ORDER BY id DESC LIMIT 1").fetchone()
    if row:
        stored_data = row[0]
        # FIXED: using parameterized query to prevent SQL injection
        query = "SELECT * FROM users WHERE info = ?"
        conn.execute(query, (stored_data,))
        results = conn.fetchall()
        conn.close()
        return str(results)
    return 'No data'

if __name__ == '__main__':
    app.run(debug=True)