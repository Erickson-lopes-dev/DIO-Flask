from flask import Flask, jsonify, request
import json
app = Flask(__name__)


@app.route('/<int:pk>')
def pessoas(pk):
    # retorna um texto em json
    return jsonify({'pk': pk, 'nome': 'Erickson', 'profissao': 'Carpinteiro'})


# @app.route('/soma/<int:v1>/<int:v2>')
# def soma(v1, v2):
#     return {'soma': v1 + v2}


@app.route('/soma/', methods=['POST', 'GET'])
def soma_post():
    if request.method == 'POST':
        dados = json.loads(request.data)
        soma = sum(dados['valores'])
        return jsonify({'soma': soma})

    elif request.method == 'GET':
        return jsonify({'message': 'Some os valores enviado como método post'})


if __name__ == '__main__':
    app.run(debug=True)
