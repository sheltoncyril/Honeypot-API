import docker
def ver():
    client=docker.from_env()
    version=client.version()
    client.close()
    return version
    


def createhoneypot(mnt):
    client=docker.from_env()
    cont= client.containers.run('php:apache', 
    detach=True,
    volumes={
        mnt:{
            'bind':'/var/www/html/',
            'mode':'rw',
            }
    },
    ports={
        '80':("127.0.0.1",None),
        }
    )
    client.close()
    return cont

def deletehoneypot(container_id):
    client=docker.from_env()
    cont=client.containers.get(container_id)
    cont.stop()
    cont.remove()
    client.close()
    return True
    
    
    
