from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevSecOps TP</h1>
    <p>Application de test de sécurité web.</p>
    <a href="/user?id=1">Rechercher un utilisateur</a>
    """

@app.route("/user")
def user():
    user_id = request.args.get("id")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    result = cursor.fetchall()
    conn.close()

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
