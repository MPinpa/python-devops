import requests, json


requests.get('http://127.0.0.1:5000') # Efetua uma chamada GET

requisicao.json() # Retona conteudo em binario


# Enviando o post

requests.post('http://127.0.0.1:5000/usuarios', 
    data=json.dumps({"Nome": "mestre", "email": "teste@teste.com.br" }), 
    headers={'content-type': 'application/json'} 
    )