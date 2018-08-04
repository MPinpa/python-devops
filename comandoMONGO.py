from pymongo import MongoClient # importa o modulo

client = MongoClient() # instancia a conexao

db = client['flask-app'] # usando a base flask-app

db.user.insert_one() # insere no banco na tabela users

db.user.find() # faz uma busca no banco de dados

usr = db.user.update_one() # atualiza um campo da tabela
usr.matched_count # quantos encontrado
usr.modified_count # quanto ele modificou

"$push" #para subs documentos  

"Mensagens.nome" # para bsucar osub documento no update ou delete

"$pull" # Deleta um sub documento