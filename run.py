import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    messages.append("{} said: {}<br>".format(username, message))

def get_all_messages():
    return "<br>".join(messages)

@app.route("/")
def index():
    return "<h1>Hello There</h1>"

@app.route("/<username>")
def user(username):
    return '<h1>Welcome {}!</h1>{}'.format(username, get_all_messages())
    
@app.route("/<username>/<message>")
def send_message(username,message):
    add_messages(username, message)
    return redirect ("/" + username)


if __name__ =="__main__":
    app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)