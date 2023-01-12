from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def welcome():
    response_text = '{"message": "Hello, welcome to Johnny\'s flask-api"}'
    response = Response(response_text, 200, mimetype='applications/json')
    return response



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)