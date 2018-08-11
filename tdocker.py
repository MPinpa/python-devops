import docker

try:
    con = docker.DockerClient('tcp://192.168.0.200:2376')
except Exception as e:
    print('Erro:{}'.format(e))
    exit()

containers = con.containers.list(all=True)


# ids = [x.short_id for x in containers]

# print(ids)

for container in containers:
     container.start()
