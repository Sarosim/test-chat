import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key=os.getenv("SECRET", "randomstring12345")
messages = []

def add_messages(username, message):
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {'timestamp': now, 'from': username, 'message': message}
    messages.append(messages_dict)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")

#@app.route("/<username>")
#def user(username):
#    return render_template("chat.html", username = username, chat_messages = messages)
    
@app.route("/chat/<username>", methods = ["GET", "POST"])
def user(username):
    """Display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_messages(username, message)
        return redirect(url_for("user", username=session["username"]))

    return render_template("chat.html", username=username,
                           chat_messages=messages)
    
if __name__ =="__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=False)
