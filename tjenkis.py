import jenkins


try:
    con = jenkins.Jenkins('127.0.0.1:8080', username='developer', password='4linux')
except Exception as e:
    print("Erro: {}".format(e))