#!/usr/bin/python3

from flask import Flask, Blueprint, jsonify, Response, request, redirect
from bson.json_util import dumps
from pymongo import MongoClient


try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print ("Erro: {}".format(e))
    exit()

app = Flask(__name__)

usuario = Blueprint('usuario', __name__)

@usuario.route('/usuarios', methods=['GET'])
def usuarios():

    user = db.user.find()

    return Response (dumps(user), status=200, content_type='application/json')

@usuario.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    user = request.get_json()
    if user['nome'] and user['email']:
        db.user.insert_one(
            {
                "nome": user["nome"],
                "email": user["email"],
                "Mensagens" : user['Mensagens']
            }
        )
        mensagem = dumps({'mensagem': 'Usuario {} cadastro com sucesso'.format(user['nome'])})
        status = 201
    else:
        
        mensagem = dumps({'mensagem' : 'Informacoes invalidas'})
        status = 400

    return Response (mensagem, status=201, content_type="application/json")

@usuario.route('/usuarios', methods=['PATCH'])
def atualizar_usuario():
    user = request.get_json()
    update = db.user.update_one(
        {"email": user['email']},
        {"$set": user}
    )

    if update.modified_count:
        mensagem = {"mensagem":"Usuario {} atualizado".format(user['nome'])}
        status = 200
    elif update.matched_count:
        mensagem = {"mensagem": "Usuario {} náo atualizado".format(user['nome'])}
        status = 400 
    else:
        mensagem = {"mensagem": "usuario nao encontrado"}
        status = 404

    return Response(dumps(mensagem), status=status, content_type='application/json')

@usuario.route('/usuarios', methods=['DELETE'])
def deletar_usuarios():
    user = request.get_json()
    remove = db.user.delete_one(
        {"email":user["email"]}
    )

    if remove.deleted_count:
        mensagem = {"mensagem": "Usuario {} removido com sucesso".format(user["nome"])}
        status = 200
    else:
        mensagem = {"mensagem": "Usuario nao escontrado"}
        status = 404

    return Response(dumps(mensagem), status=status, content_type='appication/json')