import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # VULNERABILIDADE AQUI
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login OK"
    else:
        return "Login falhou"

if __name__ == "__main__":
    app.run(debug=True)
