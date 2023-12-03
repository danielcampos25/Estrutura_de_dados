class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

raiz = ArvoreBinaria(2, ArvoreBinaria(1), ArvoreBinaria(3))


def constituiArvoreBinariaDeBusca(raiz):
    def inorder_list(ab):
        result_list = []
        if ab.esq:
            result_list.extend(inorder_list(ab.esq))
        result_list.append(ab.dado)
        if ab.dir:
            result_list.extend(inorder_list(ab.dir))
        return result_list
    listak = inorder_list(raiz)
    for i in range(len(listak)-1):
        if listak[i+1]<listak[i]:
            return False

  

constituiArvoreBinariaDeBusca(raiz)
        
        