# server.py
from flask import Flask, jsonify
from aternos import Client

app = Flask(__name__)

EMAIL = "richer.moni777@gmail.com"
PASSWORD = "543regeon"

@app.route("/start", methods=["POST"])
def start_server():
    try:
        at = Client()
        at.login(EMAIL, PASSWORD)

        server = at.account.servers[0]  # если у тебя 1 сервер
        if server.status != "online":
            server.start()
            return jsonify({"message": "Сервер запускается..."})
        else:
            return jsonify({"message": "Сервер уже включён."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()