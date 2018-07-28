from flask import Flask, make_response

conteudo.json() # transforma conteudo em um json, se tive a sintax correta


make_response(json.dumps(conteudo), 404, headers) # Simula o erro


# blueprints

# Organiza todas as rotas, melhor que colocar em um unico arquivo
# e ficar dificil manutencao

usuario = Blueprint('usuario', __name__) # Define o Blueprint
@usuario.route('/') # Define a rota