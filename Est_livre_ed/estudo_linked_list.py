class Node:
    def __init__(self,dataInit):
        self.data = dataInit
        self.next = None




class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,elem): #Adicionando itens na linked list
        if self.head: # Caso em que já existem elementos na lista
            pointer = self.head #Caminhar na lista
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else: #Caso estejamos adicionando o primeiro item na lista
            self.head = Node(elem)       #A cabeça passa agora a ser o elemento que inserimos
        self.size+=1

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        pointer = self.head  #pointer começa na cabeça da lista
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            #Agora com o pointer na posição adequada:
            if pointer:
                return pointer.data
            raise IndexError("list index out of range")

    def __setitem__(self,index,elem):
        pointer = self.head  #pointer começa na cabeça da lista
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            #Agora com o pointer na posição adequada:
            if pointer:
                pointer.data = elem
            else:
                raise IndexError("list index out of range")

    def index(self,elem):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i 
            else:
                pointer = pointer.next
                i+=1
        raise ValueError(f"{elem} is not in the list")

    def insert(self, index, elem): # inserir um elemento em uma posição especifica da lista 
        #dois casos: inserir no head ou não
        if index ==0:
            node = Node(elem)
            node.next = self.head
            self.head = node
        pointer = self._getnode(index-1)
        node = Node(elem)
        pointer.next = 
        

    def _getnode(self,index):
        pointer = self.head
        for _ in range(index-1):
            if pointer:
                pointer = pointer.next
            raise IndexError("Index out of range")
        return pointer

    


        

