from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    result = calc(1, 2)
    return "<p>Hello, World!</p>"


def calc(x: int, y: int) -> int:
    return x+y


if __name__ == '__main__':
    app.run()
