import jenkins
from pprint import pprint

try:
    con = jenkins.Jenkins('http://127.0.0.1:8080', username='developer', password='4linux')
except Exception as e:
    print("Erro: {}".format(e))
    exit()


con.reconfig_job('451`- exemplo', xml)

# job_xml = con.get_job_config('451 - exemplo')
# pprint(job_xml)

# pprint(con.get_all_jobs())


# queue = con.build_job('45 - exemplo')
# pprint(con.get_queue_item(queue))

# con.create_job('451 - exemplo', jenkins.EMPTY_CONFIG_XML) 

# pprint(con.get_whoami())
# pprint(con.get_version())