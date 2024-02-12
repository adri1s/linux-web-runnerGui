import sys
import subprocess
from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)

def read_conf():
    with open(f'config.yaml','r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader) 
        return data

@app.route("/")
def helloworld():
    return jsonify("Welcome to remote run") 

@app.route("/app/<page>")
def index(page):
    for app in read['Runner']:
        if page==app['name']:
            subprocess.call(app['cmd'], shell=True)
            go = app["name"]
    return '', 200 

read = read_conf()
bind = read['Bind']
port = read['Port']

if __name__ == "__main__":
    app.run(host=bind, port=port)
