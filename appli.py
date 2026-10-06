from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevSecOps TP</h1>
    <p>Application de test de sécurité web.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
