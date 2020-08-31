import json

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


class Dev(Resource):
    def get(self, id):
        try:
            desenvolvedor = desenvolvedores[id]
            print(desenvolvedor)
            return jsonify(desenvolvedor)
        except Exception as ex:
            return jsonify({'status': f'não encontrado {ex}'})

    def put(self, id):
        dados = json.loads(request.data)
        print(dados)
        desenvolvedores[id] = dados
        return jsonify(dados)

    def delete(self, id):
        desenvolvedores.pop(id)
        return jsonify({'status': 'delete'})


class ListaDev(Resource):
    def get(self):
        return jsonify({'devs': desenvolvedores})

    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)

        return jsonify({'sucess': 'dados adicionados'})


api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(ListaDev, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
