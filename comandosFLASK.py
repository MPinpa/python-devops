from flask import Flask, make_response, jsonify

conteudo.json() # transforma conteudo em um json, se tive a sintax correta


make_response(json.dumps(conteudo), 404, headers) # Simula o erro

jsonify(json) # jsonify e otimo, pois nao precisa utilizar o cabecalho json e ele mesmo ja dar um dump

# blueprints

# Organiza todas as rotas, melhor que colocar em um unico arquivo
# e ficar dificil manutencao

usuario = Blueprint('usuario', __name__) # Define o Blueprint
@usuario.route('/') # Define a rota

render_template() # renderiza um html