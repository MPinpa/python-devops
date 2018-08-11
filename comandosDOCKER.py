#Para Docker se comunicar com outra maquina

import docker # importa o modulo

con = docker.DockerClient('tcp://192.168.0.200:2376') # instancia o cliente


# cria um container com iamgem do debian
container = con.containers.run(
    'debian','/bin/bash',
    name='imagepython', detach=True,
    tty=True, ports={'5000/tcp':'5000'}
)

container = con.containers.list(all=True) # lista de container

# operacao

# cada container e um objeto no python e possui todas funcoes de liga e desliga

container.start()
container.stop()
container.stats(stream=False)
container.attach()
container.remove()
