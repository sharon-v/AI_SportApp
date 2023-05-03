from flask import Flask, request, jsonify

from testing import squatDetect

app = Flask(__name__)

@app.route('/')
def index():
    squatDetect()
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
