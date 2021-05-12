import docker

client = docker.from_env()

def netuserinput():
    netted = input(" Network Name: ")
    return netted

network = netuserinput()
client.networks.create(name=network, driver="overlay", scope="swarm")
