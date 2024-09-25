from flask import Flask, jsonify, request, make_response
from bd import Jogos

app = Flask(__name__) #O nome do módulo será assumido pelo nome do arquivo
app.json.sort_keys = False

#GET
@app.route('/jogos', methods=['GET']) #O /jogos no método GET, irá
def get_jogos(): #Nesta função
    return jsonify(
        Mensagem= 'Lista de Jogos.',
        Dados=Jogos) #Retornar a lista de jogos lá do arquivo bd

#POST
@app.route('/jogos', methods=['POST'])
def create_jogos():
    jogo = request.json
    Jogos.append(jogo) #O jogo cujos dados forem informados, será acrescentado ao final da lista Jogos, no arquivo bd
    return make_response(
        jsonify(
            Mensagem='Jogo cadastrado com sucesso!',
            Jogo=jogo
        )
    )

#PUT




app.run() #Para iniciar a api, deixá-la disponível para ser acessada, usamos esse código