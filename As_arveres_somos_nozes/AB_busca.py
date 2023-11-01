class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BT:
    def __init__(self,elem = None, node = None):
        if node:
            self.root = node
        elif elem is None:
            self.root = None
        else:
            node = Node(elem)
            self.root = node

    def symmetric_traversal(self,node = None):
        if node is None:
            node = self.root
        if node.left:
            self.symmetric_traversal(node.left)
        print(node.data)
        if node.right:
            self.symmetric_traversal(node.right)

    def postoder_traversal(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postoder_traversal(node.left)
        if node.right:
            self.postoder_traversal(node.right)
        print(node.data)

class BinarySearchTree (BT):
    def insert(self,value):
        parent = None
        aux = self.root
        while aux is not None:
            parent = aux
            if value < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = Node(value) 
        elif value<parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    '''def search(self,value,node = 0):
        if node == 0:
            node = self.root
        if node is None or node.data == value:
            return BinarySearchTree(node)                     Primeira opção de implementação de busca
        if value< node.data:
            return self.search(value,node.left)
        else:
            return self.search(value,node.right)'''


    def search(self,value):
        return self._search(value,self.root)



    def _search(self,value,node):
       
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value< node.data:
            return self.search(value,node.left)
        else:
            return self.search(value,node.right)





        
