import docker

client = docker.from_env()

servs = client.services.list(filters='id')

print(servs)
