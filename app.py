import os

from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """add messages to the messages list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """Get all messages and separate them with a `br`"""
    return "<br>".join(messages)




@app.route('/')
def index():
    """Main page with instructions"""
    return "to send a message use /USERNAME/MESSAGE"


@app.route('/<username>')
def user(username):
    """display chat messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """create new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
