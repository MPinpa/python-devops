#!/usr/bin/python3

import requests, json


headers = {'content-type': 'application/json'}

data = {
    "nome": "Mestre",
    "email": "papa@teste"
}

requisicao = requests.delete('http://127.0.0.1:5000/usuarios/3', headers=headers)



print(requisicao)