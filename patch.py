#!/usr/bin/python3

import requests, json

data = {
    "nome": "joao",
    "sobrenome": "hummel"
}

requisicao = requests.get('http://127.0.0.1:5000/exemplo')

conteudo = requisicao.json()
print(conteudo['message'])