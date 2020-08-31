import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Erickson',
     'habilidades': ['python', 'Flask']},
    {'nome': 'Daniel',
     'habilidades': ['Piloto', 'Arruma role']},
    {'nome': 'Renan',
     'habilidades': ['Motorista', 'Evangélico']},
    {'nome': 'Leticia',
     'habilidades': ['python', 'flask']},
]


# @app.route('/dev/', methods=['GET'])
# def desenvolvedor():
#     return jsonify({'nome': 'Erickson'})

# retorna um dev e altera ou deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor_procurar(id):
    if request.method == 'GET':
        try:
            desenvolvedor = desenvolvedores[id]
            print(desenvolvedor)
            return jsonify(desenvolvedor)
        except Exception as ex:
            return jsonify({'status': f'não encontrado {ex}'})

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        print(dados)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({'status': 'delete'})


# lista todos os dev e cria um novo
@app.route('/dev/', methods=['GET', 'POST'])
def lista_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)

        return jsonify({'sucess': 'dados adicionados'})
    if request.method == 'GET':
        return jsonify({'devs': desenvolvedores})


if __name__ == '__main__':
    app.run(debug=True)
