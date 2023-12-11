class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    def addNeighbor(self,nbr,weight=1):
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
        self.peso_total = 0
    def addVertex(self,key):
        self.vertNum+=1
        if key not in self.vertList:
            newVertex = Vertex(key)
            self.vertList[key] = newVertex
            return newVertex
        else:
            return None

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, v1, v2, weight):
        # Certifique-se de que ambos os vértices existam no grafo
        if v1 not in self.vertList:
            nv1 = self.addVertex(v1)
        if v2 not in self.vertList:
            nv2 = self.addVertex(v2)

        # Verifica se a ligação já existe
        if v2 not in self.vertList[v1].getConnections():
            # Se não existir, adiciona a ligação
            self.peso_total += weight
            self.vertList[v1].addNeighbor(self.vertList[v2], weight)
            # Atualiza o peso_total

   
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
    
    
    
    
def encontrar_caminhos(grafo, i, j, visitados=None):
    if visitados is None:
        visitados = set()

    ni = grafo.getVertex(i)
    nf = grafo.getVertex(j)
    caminhos = []

    if ni is None or nf is None:
        return []

    visitados.add(ni.getId())

    if i == j:
        return [[i]]

    for v in ni.getConnections():
        if v.getId() == j and v.getId() not in visitados:
            caminhos.append([ni.getId(), v.getId()])
        elif v.getId() not in visitados:
            caminhos_intermediarios = encontrar_caminhos(grafo, v.getId(), j, visitados.copy())
            for caminho in caminhos_intermediarios:
                caminho.insert(0, ni.getId())
                caminhos.append(caminho)

    return caminhos


n = int(input())
grafo = Graph()
for _ in range(n):
    entrada = input().split()
    id = entrada[0]
    grafo.addVertex(id)
    lista = entrada[2:]
    print(lista)
    for i in range(0,len(lista), 2):
        grafo.addEdge(id,lista[i+1],int(i))
    
    
print(grafo.peso_total)