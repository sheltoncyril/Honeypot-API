import docker

def ver():
    client=docker.from_env()
    ret = client.version()
    client.close()
    return ret

def create(sargs):
