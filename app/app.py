#!/usr/bin/python3

from flask import Flask, Response, jsonify
import json
from blueprints.usuarios import usuario

app = Flask(__name__)
app.register_blueprint(usuario)


@app.route('/', methods=['GET', 'POST'])
def index():
 #   headers = {"content-type": "application/json"}

    retorno = {
        "message":  "resposta usando make_response"
    }
    return Response(json.dumps(retorno), 404, content_type="application/json")

@app.route('/arquivo', methods=['GET'])
def arquivo():

    with open('nomes.txt', 'r') as arq:
        retorno = {'nomes':[x.replace('\n', '') for x in arq.readlines()]}

    return jsonify(retorno)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)