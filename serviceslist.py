import docker
from docnodelist import NodeList
from docnodelist import NodeReturn

client = docker.from_env()

class Nodes(NodeList):
    #pass
    def __init__(self):
        super(Nodes, self).__init__()

class ServicesList(NodeReturn):

    def __init__(self):
        super(NodeReturn, self).__init__()

    def manager_list(self):
        service1 = self.managers
        for node in service1:
            #service1 = ("id: {}".format(node))
            service1 = client.services.list()
            service2 = service1.("id: {}".format(node))
            service3 = service2.split()
            service4 = service3.pop(2)
            services = service4.replace(">", "")
            print(services)

    def worker_list(self):
        service1 = self.workers
        for node in service1:
            service1 = client.services.list()
            service1 = ("id: {}".format(node))
            service2 = service1.split()
            service3 = service2.pop(-1)
            services = service3.replace(">", "")
            print(services)



listing = ServicesList()
print(listing.manager_list())
print(listing.worker_list())
