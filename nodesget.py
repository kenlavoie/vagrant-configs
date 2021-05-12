import docker
import docnodelist

client=docker.from_env()

nodes = docnodelist.NodeReturn()
print(nodes)
