import paramiko

try:
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.0.200', 
                    username='root', 
                    password='4linux'
                    )

except Exception as e:
    print('Erro conexao: {}'.format(e))