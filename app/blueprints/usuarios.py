#!/usr/bin/python3

from flask import Flask, Blueprint, jsonify

app = Flask(__name__)

usuario = Blueprint('usuario', __name__)

@usuario.route('/usuarios')
def user():

    with open('cont', 'r') as arq:
        conteudo = int(arq.readline())
        conteudo += 1
    with open('cont', 'w') as arq:
        arq.write(str(conteudo))

    return 'Numero de vezes que a pagina foi acessada: {}'.format(conteudo)