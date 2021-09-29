from flask import Flask

# Hello Everyone
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello everyone !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'


if __name__ == '__main__':
    app.run()
