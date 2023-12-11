class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

class BT:
    def __init__(self,data = None,node = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None


    def percurso_emordem(self,node = None):
        if node is None:
            node = self.root
        if node.left:
            self.percurso_emordem(node.left)
        print(node)
        if node.right:
            self.percurso_emordem(node.right)

    def percurso_preordem(self,node=None):
        if node is None:
            node = self.root
        print(node)
        if node.left:
            self.percurso_preordem(node.left)
        if node.right:
            self.percurso_preordem(node.right)

    def percurso_posordem(self,node= None):
        if node is None:
            node = self.root
        if node.left:
            self.percurso_posordem(node.left)
        if node.right:
            self.percurso_posordem(node.right)
        print(node)

   


class BST(BT):
    def inserir(self,value):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if value< aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = Node(value)
        elif value< parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
#criando funçoes que recebem arvores como parametros            

def inverteAB(raiz):
    def i(node):
        if node is not None:
            node.left,node.right = node.right,node.left
            i(node.left)
            i(node.right)
        return node
    raiz = i(raiz)

    


def verifica_simetriaAB(raiz):
    def espelho(aesq,adir):
        if aesq is not None and adir is not None:
            if aesq.data== adir.data and espelho(aesq.left,adir.right) and espelho(aesq.right,adir.left):
                return True
            else:
                return False
        else:
            return True
    
    
    if raiz is None:
        return True
    else:
        return espelho(raiz.left,raiz.right)

arvore = BST()
arvore.inserir(10)
arvore.inserir(21)
arvore.inserir(30)
arvore.inserir(3)
arvore.inserir(14)
arvore.inserir(5)

raiz = Node(1)
raiz.left = Node(2)
raiz.right = Node(2)
raiz.left.left = Node(3)
raiz.left.right = Node(5)
raiz.right.right = Node(3)
raiz.right.left = Node(5)
raiz.left.left.left = Node(9)
raiz.right.right.right = Node(9)

if verifica_simetriaAB(raiz):
    print('ok')
else:
    print('nao é')