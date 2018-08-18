import requests
from pprint import pprint

token = 's-qnh9vMoTTRTKr7YGSh'

id_projeto = 2

url = 'http://127.0.0.1/api/v4/projects/{}/members?private_token={}'.format(id_projeto, token)



post = {
    'user_id': 2,
    'access_level': 40,

}




# post = {
#     'email': 'cassiano@master.com.br',
#     'username': 'cassianodantas',
#     'name': 'cassiano lima dantas',
#     'password': '12345678'
#  }


usuarios = requests.post(url, post)

pprint(usuarios.json())

#url = 'http://127.0.0.1/api/v4/projects?private_token={}'.format(token)

# post = {
#     'name': 'flask-app'
# }

#projetos = requests.post(url, post)


# projetos = requests.get(url)

# pprint(projetos.json()[0]['name'])