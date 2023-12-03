class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if value>aux.data:
                aux = aux.right
            else:
                aux = aux.left
        if parent is None:
            self.root = Node(value)
        elif value>parent.data:
            parent.right = Node(value)
        elif value<parent.data:
            parent.left = Node(value)
    
    def inorder(self,node = None): #esquerda -> raiz -> direita
        if node is None:
            node = self.root
        
        if node.left:
            self.inorder(node.left)
        print(node.data, end = ' ')
        if node.right:
            self.inorder(node.right)

    def preorder(self,node = None): #raiz => esquerda => direita
        if node is None:
            node = self.root
        print(node.data, end = ' ')
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
    
    def postorder(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.data, end = ' ')

AB = BST()
AB_vazia = True
while True:
    user_input = input()
    
    try:
        number = int(user_input)
        AB.insert(number)
        AB_vazia = False

    except ValueError:
        if user_input == 'in':
            if AB_vazia:
                print()
            else:
                AB.inorder()
                print()
        elif user_input == 'pre':
            if AB_vazia:
                print()
            else:
                AB.preorder()
                print()
        elif user_input == 'pos':
            if AB_vazia:
                print()
            else:
                AB.postorder()
                print()
        elif user_input == 'quack':
            break



