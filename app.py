from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/1')
def hello_world1():
    return 'Hello, another route!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2100)