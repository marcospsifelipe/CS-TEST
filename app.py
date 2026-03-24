import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

"""
Aplicação de teste com vulnerabilidades intencionais.
Usado para simular detecção SAST na plataforma da Conviso.

Vulnerabilidades incluídas:
- SQL Injection
- Command Injection
"""

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # Vulnerabilidade: SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login OK"
    else:
        return "Login falhou"


@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Vulnerabilidade: Command Injection
    return os.popen("ping -c 1 " + host).read()


if __name__ == "__main__":
    app.run(debug=True)
