from fila import Queue
 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
class BT:
    def __init__(self,data= None):
        
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    
    def ordem_simetrica(self,node=None):
            if node is None:
                node = self.root
            if node.left:
                self.ordem_simetrica(node.left)
            print(node)
            if node.right:
                self.ordem_simetrica(node.right)
    def pos_ordem(self,node = None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_ordem(node.left)
        if node.right:
            self.pos_ordem(node.right)
        print(node)

    def pre_order(self,node = None):
        if node is None:
            node = self.root
        print(node)
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    def altura(self,node = None):
        if node is None:
            node = self.root
        if node is None:
            return 0 
        else:
            hleft = 0
            hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)
        if hleft>hright:
            return hleft+1
        else:
            return hright+1

    def percurso_nivel(self,node = None):
        if node is None:
            node = self.root
        else:
            fila = Queue()
            fila.push(node)
            while len(fila)>0:
                pass


class BST(BT):
    def insert(self,value):
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
    
    
    def remove(self,value,node = None):
        if node is None:
            node = self.root
        if node is None:
            return None
        if value>node.data:
            self.remove(value,node.right)
        if value<node.data:
            self.remove(value,node.left)
        else: #se value == node.data
            
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            else:
                substituto = self.min(node.right)
                node.data = substituto
                node.right = self.remove(substituto,node.right)

        return node.data

    
    
    
    
    
    
    
    
    
    
    def min(self,node = None):
        if node is None:
            node = self.root
        
        while node.left:
            node = node.left

        return node.data

    def max(self,node = None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right

        return node.data

    


    
