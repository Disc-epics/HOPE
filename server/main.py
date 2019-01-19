from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    '''
    Make / an alias to static/index.html
    '''
    return send_from_directory('static', 'index.html')
