from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/<int:pk>')
def pessoas(pk):
    # retorna um texto em json
    return jsonify({'pk': pk, 'nome': 'Erickson', 'profissao': 'Carpinteiro'})


@app.route('/soma/<int:v1>/<int:v2>')
def soma(v1, v2):
    return {'soma': v1 + v2}


@app.route('/soma/', methods=['POST'])
def soma_post():
    return jsonify({'soma': 'soma'})


if __name__ == '__main__':
    app.run(debug=True)
