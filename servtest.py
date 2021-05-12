import docker
#from docnodelist import NodeList
#from docnodelist import NodeReturn

client = docker.from_env()
managers = client.nodes.list( filters={'role': 'worker'})

def manager_node_listing():
    for node in managers:
        output1 = ("manager node: {}".format(node))
        output2 = output1.split()
        output3 = output2.pop(3)
        output = output3.replace(">", "")
        print(output)
    #return(output)

print(manager_node_listing())
