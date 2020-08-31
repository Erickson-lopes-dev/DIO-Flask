from flask import Flask

app = Flask(__name__)


@app.route('/')
def pessoas():
    return {'nome': 'Erickson'}


if __name__ == '__main__':
    app.run(debug=True)
