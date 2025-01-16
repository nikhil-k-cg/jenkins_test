from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """
    home fun
    """
    return "<h1>Welcome to Webhook demo!!!<h1/>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
