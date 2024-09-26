from flask import Flask, jsonify, request, make_response
from bd import Jogos

app = Flask(__name__)
app.json.sort_keys = False

#GET
@app.route('/jogos', methods=['GET'])
def get_jogos():
    return jsonify(
        Mensagem= 'Lista de Jogos',
        Dados=Jogos)

#GET_BY_ID
@app.route('/jogos/<int:id>', methods=['GET'])
def get_by_id(id):
    for jogo in Jogos:
        if jogo.get('id') == id:
            return jogo
    return jsonify(
        Mensagem='Não há jogo com este id.'
    )
        
#GET_BY_YEAR
@app.route('/jogos/ano/<int:ano_lancamento>', methods=['GET'])
def get_by_year(ano_lancamento):
    by_year = []
    for jogo in Jogos:
        if jogo.get('ano_lancamento') == ano_lancamento:
            by_year.append(jogo)
    return jsonify(
        Mensagem = f'Os jogos lançados no ano de {ano_lancamento} são:',
        Jogos = by_year
        )

#POST
@app.route('/jogos', methods=['POST'])
def create_jogos():
    jogo = request.json
    Jogos.append(jogo)
    return jsonify(
        Mensagem='Jogo cadastrado com sucesso!',
        Jogo=jogo
    )

#PUT
@app.route('/jogos/<int:id>', methods=['PUT'])
def update_jogos(id):
    jogo_alterado = request.get_json()
    for indice, jogo in enumerate(Jogos):
        if jogo.get('id') == id:
            Jogos[indice].update(jogo_alterado)
            return jsonify(Jogos[indice])

#DELETE
@app.route('/jogos/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    for indice, jogo in enumerate(Jogos):
        if jogo.get('id') == id:
            del Jogos[indice]
            return jsonify(
                Mensagem = 'O jogo foi excluído com sucesso.'
            )
    return jsonify(
        Mensagem='Não há jogo com este id.'
    )

app.run()