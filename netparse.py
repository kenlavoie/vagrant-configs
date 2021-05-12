import docker

client = docker.from_env()

node_list = client.nodes.list( filters={'role': 'worker'})

def node_listing():
    for node in node_list:
        if node in node_list:
            print(node)
    else:
        print("/end")

#node_listing()
