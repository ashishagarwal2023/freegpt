from flask import Flask, jsonify, render_template, request
from api.gpt import Bot

app = Flask(__name__)

bot = Bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/token", methods=["POST"])
def api_new():
    tokenNew = request.form.get("token")
    if bot.verify(tokenNew):
        bot.token(tokenNew)
        return jsonify({"message": "Successfully changed bot token."}), 200
    else:
        return jsonify({"error": "Invalid token or token is rate limited"}), 400

@app.route("/api/prompt", methods=["POST"])
def api_prompt():
    prompt = request.form.get("prompt")
    try:
        resp = bot.prompt(prompt)
        return jsonify({"response": resp}), 200
    except:
        return jsonify({"error": "Server-related error, the token could have been rate limited. If you didn't specify a token, please specify it."}), 500

@app.route("/api/reset", methods=["POST"])
def api_reset():
    bot.token("") # For those thinking what's wrong here, changing token resets conversation too, or just bot.reset()
    return jsonify({"message": "Successfully reset bot conversation."}), 200