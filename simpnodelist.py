import docker

client = docker.from_env()


class NodeList(object):
    """
    This pulls the nodes via the the SDK nodes.list
    """

    def __init__(self):
        self.workers = client.nodes.list( filters={'role': 'worker'})
        self.managers = client.nodes.list( filters={'role': 'manager'})


class NodeReturn(NodeList):
    """
    Returns the appropriate manager/worker node. Returns only the nodes, and no
    other value. Name, manager/worker are not listed
    """
    def manager_node_listing(self):
        managers = self.managers
        for node in managers:
            output1 = ("manager node: {}".format(node))
            output2 = output1.split()
            output3 = output2.pop(3)
            output = output3.replace(">", "")
            print(output)
        else:
            print("end of manager list, no nodes found")


    def worker_node_listing(self):
        workers = self.workers
        for node in workers:
            output1 = ("worker node: {}".format(node))
            output2 = output1.split()
            output3 = output2.pop(3)
            output = output3.replace(">", "")
            print(output)
        else:
            print("end of worker list, no nodes found")

nodes = NodeReturn()
print(nodes.manager_node_listing())
print(nodes.worker_node_listing())
