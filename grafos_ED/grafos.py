class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.vertNum = 0
    def addVertex(self,key):
        self.vertNum+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self,v1,v2,weight =0):
        if v1 not in self.vertList:
            nv1 = self.addVertex(v1)
        if v2 not in self.vertList:
            nv2 = self.addVertex(v2)
        self.vertList[v1].addNeighbor(self.vertList[v2],weight)

    def getVertices(self):
        return self.vertList.keys()

    def caminho(self,key1,key2):
        inicio = self.getVertex(key1)
        fim = self.getVertex(key2)
        if inicio == None or fim == None:
            return None
        for elems in inicio.getConnections():
            if elems.getId()== key2:
                return [inicio.getId(),elems.getId()]
            caminhoFinal = self.caminho(elems.getId(),key2)
        if caminhoFinal != None:
            caminhoFinal.insert(0,inicio.getId())
            return caminhoFinal
        return None
