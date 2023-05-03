from flask import Flask, request, jsonify

from testing import squatDetect

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    squatDetect()
    data = request.get_json()
    message = data['message']
    response = {'status': 'OK', 'message': message}
    return jsonify(response)

@app.route('/')
def index():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()
