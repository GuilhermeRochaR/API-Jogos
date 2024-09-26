from flask import Flask, jsonify, request, make_response
from bd import Jogos

app = Flask(__name__) #O nome do módulo será assumido pelo nome do arquivo
app.json.sort_keys = False

#GET
@app.route('/jogos', methods=['GET']) #O /jogos no método GET, irá
def get_jogos(): #Nesta função
    return jsonify(
        Mensagem= 'Lista de Jogos',
        Dados=Jogos) #Retornar a lista de jogos lá do arquivo bd

#GET_BY_ID
@app.route('/jogos/<int:id>', methods=['GET'])
def get_by_id(id):
    for jogo in Jogos:
        if jogo.get('id') == id:
            return jogo
        
#GET_BY_YEAR
@app.route('/jogos/ano/<int:ano_lancamento>', methods=['GET'])
def get_by_year(ano_lancamento):
    by_year = []
    for jogo in Jogos:
        if jogo.get('ano_lancamento') == ano_lancamento:
            by_year.append(jogo)
    return make_response(
        jsonify(
            Mensagem = f'Os jogos lançados no ano de {ano_lancamento} são:',
            Jogos = by_year
        )
    )


#POST
@app.route('/jogos', methods=['POST'])
def create_jogos():
    jogo = request.json
    Jogos.append(jogo) #O jogo cujos dados forem informados, será acrescentado ao final da lista Jogos, no arquivo bd
    return jsonify(
        Mensagem='Jogo cadastrado com sucesso!',
        Jogo=jogo
    )

#PUT
#@app.route('/jogos/<int:id>', methods=['PUT'])

#DELETE
#@app.route('/jogos/<int:id>', methods=['DELETE'])



app.run() #Para iniciar a api, deixá-la disponível para ser acessada, usamos esse código