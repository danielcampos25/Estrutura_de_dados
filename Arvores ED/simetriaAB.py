class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            node = Node(data)
            self.root = node

    def insert(self, value):
        aux = self.root
        parent = None
        while aux:
            parent = aux
            if value > aux.data:
                aux = aux.right
            else:
                aux = aux.left

        if parent is None:
            self.root = Node(value)
        elif value > parent.data:
            parent.right = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            # Handle the case where the value is equal to the current node's value
            # You can choose to ignore, update, or handle it according to your requirements.
            pass




def verificaSimetria(raiz):
    def compara(a_esq, a_dir):
       
        if not a_esq and not a_dir:
            return True

        
        if a_esq and a_dir and a_esq.data == a_dir.data:
            
            return compara(a_esq.left, a_dir.right) and compara(a_esq.right, a_dir.left)

        return False

    return compara(raiz.left, raiz.right)



def busca_nivel(raiz,value,n=0):
    if raiz is None:
        return None
    node = raiz
    if value > node.data:
        return busca_nivel(node.right,value,n+1)
    elif value < node.data:
        return busca_nivel(node.left,value,n+1) 
    elif value == node.data:
        return n
    else:
        return None
    
numeros = [60,14,3,5,87,134,23,45,20,6,7,8,9,10,11,12]
ab = BST()

for elem in numeros:
    ab.insert(elem)


print(busca_nivel(ab.root,12))