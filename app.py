from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DB")
    )

@app.route("/")
def home():
    return "🚀 Flask + MySQL CI/CD Pipeline Working!"

@app.route("/db")
def db_test():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Database Connected!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"message": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
