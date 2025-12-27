from flask import Flask
 requests
import os

app = Flask(__name__)

BOT = "8438796872:AAEtrjfPgsjIEYjRdjWnJRkfqu6CGC4KQxk"
CHAT = "7628413315"

@app.route("/")
def home():
    requests.post(
        f"https://api.telegram.org/bot{BOT}/sendMessage",
        json={"chat_id": CHAT, "text": "✅ Render server is alive"}
    )
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
