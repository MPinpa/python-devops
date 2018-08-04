from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

try:
    client = MongoClient()
    db = client['flask-app']
except Exception as e:
    print("Erro: {}".format(e))
    exit()
# deletando um subdocumento
user= db.user.update_one(
    {"_id":ObjectId('5b65a430199a911514c7fe45')},
    {
        "$pull":{
            "mensagens":{
                "nome":"daniel",
        }
    }}
)
print(user.matched_count, user.modified_count)
user= db.user.update(
#     {"mensagens.nome":"novousuario"},
#     {
#         "$set":{
#             "mensagens.$.nome":"daniel"

#         }
#     }
# )
# user= db.user.update_one(
#     {"_id":ObjectId('5b65a430199a911514c7fe45')},
#     {
#         "$push":{
#             "mensagens":{
#                 "nome":"novousuario",
#                 "mensagem":"novamensagem"}

#         }
#     }
# )
# user= db.user.delete_one(
#     {"_id":ObjectId('5b65a430199a911514c7fe45')}
# )
# print(user.deleted_count)
# print(db.user.find_one({"_id":ObjectId('5b65a430199a911514c7fe45')}))
# user = db.user.update_one(
#     {"nome":"danielprata"},
#     {"$set":{
#         "email":"danielprata@outlook.com.br"
#     }}

# )
# print(user.matched_count, user.modified_count)


# users = [x for x in db.user.find({'nome':'danielprata'})]
# print(user["_id"].generation_time)
# db.user.insert_one(
#     {
#         "nome":"danielprata",
#         "email":"daniel.prata@4linux.com.br",
#         "mensagens":[
#             {
#                 "nome":"usuario",
#                 "mensagem":"mensagem"
#             },
                # {
#                 "nome":"usuario",
#                 "mensagem":"mensagem"
#             },

#         ]

#     }
# )