pip3 install python-jenkins
ou
pip3 install jenkins


import jenkis

con = jenkins.Jenkins('127.0.0.1:8080', username='developer', password='') # instancia a conexao

con.get_whoami() # Traz informacoes do usuario logado

con.get_version() # traz informacoes da versao do jenkins

con.create_job('451 - exemplo', jenkins.EMPTY_CONFIG_XML) # cria uma job

con.get_all_jobs() # Lista todos os jobs

job_xml = con.get_job_config('451 - exemplo') # traz o xml de um job

con.reconfig_job('451 - exemplo', xml) # reconfigura o job

con.build_job('451 - exemplo')