from pymongo import MongoClient
from bson.objectid import ObjectId

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print ("Erro: {}".format(e))
    exit()


users = db.user.update_one(
    {"Mensagens.nome": "novousuario2"},
    {
        "$set":{
            "Mensagens.$.nome":"daniel"
        }
    }
)
    

print ()


