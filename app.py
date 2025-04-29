from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is practical no 13 about Python Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
