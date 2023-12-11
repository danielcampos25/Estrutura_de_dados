class Vertice:
    def __init__(self,key):
        self.id = key
        self.conectado = {}
    def adicionarVizinho(self,vizinho,peso=0):
        self.conectado[vizinho] = peso
    def obterConexoes(self):
        return self.conectado.keys()
    def obterId(self):
        return self.id
    def obterPeso(self,vizinho):
        return self.conectado[vizinho]

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numero_vertices = 0

    def adicionarVertice(self,key):
        self.numero_vertices +=1
        novo_vertice = Vertice(key)
        self.listaVertices[key] = novo_vertice
        return novo_vertice

    def obterVertice(self,key):
        if key in self.listaVertices:
            return self.listaVertices[key]
        else:
            return None #vertice inexistente

    def adcionarAresta(self,v1,v2,peso = 0):
        if v1 not in self.listaVertices:
            nv1 = self.adicionarVertice(v1)
        if v2 not in self.listaVertices:
            nv2 = self.adicionarVertice(v2)
        self.listaVertices[v1].adicionarVizinho(self.listaVertices[v2],peso)

    def obterVertices(self):
        return self.listaVertices.keys()

    def caminho(self,key1,key2): #Busca apenas um caminho
        inicio = self.obterVertice(key1)
        fim = self.obterVertice(key2)
        if inicio == None or fim == None:
            return None
        for elems in inicio.obterConexoes():
            if elems.obterId()==key2:
                return [inicio.obterId(),elems.obterId()]
            caminhoFinal = self.caminho(elems.obterId(),key2)
        if caminhoFinal!= None:
            caminhoFinal.insert(0,inicio.obterId())
            return caminhoFinal
        return None

    #função