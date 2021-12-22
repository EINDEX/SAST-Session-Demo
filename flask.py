import subprocess
import flask
from flask import request
from tools import escape, fake_escape

app = flask.Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', "World")
    return """
    <h1>Hello, {name}!</h1>
    <form method="get">
    <span>What is your name?</span>
    <input type="text" name="name"/>
    <br>
    <input type="submit" value="Submit">
    <hr>
    </form>
    <form action="/ping" method="get">
    <span>Ping Host</span>
    <input type="text" name="cmd"/>
    <br>
    <input type="submit" value="Submit">
    </form>
    """.format(name=name)

@app.route("/ping")
def ping():
    location = request.args.get('cmd', "127.0.0.1")
    stdoutdata = subprocess.getoutput("ping -c 2 " + location)
    return stdoutdata.replace("\n", "<br>")

@app.route('/')
def looks_bad_and_bed():
    name = request.args.get('name', "World")
    return fake_escape(name)

@app.route('/')
def looks_bad_but_ok():
    name = request.args.get('name', "World")
    return escape(name)

app.run(host="0.0.0.0", port=8080, debug=True)
