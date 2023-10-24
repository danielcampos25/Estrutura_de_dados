#last in first out

class Node:
    def __init__(self,dataInit):
        self.data = dataInit
        self.next = None




class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,elem):
        #inserir um elemento na pilha
        node = Node(elem)   # cada nó deve "saber" quem está imediatamente "embaixo" dele
        node.next = self.top # pensar o .next como "abaixo" ao inves de "proximo"
        self.top = node
        self._size+=1

    
    def pop(self):
        #remover e retornar o elemento do topo da lista
        if self._size > 0:
            node = self.top #elemento que desejamos tirar e retornar da pilha
            self.top = self.top.next # operação que move o self top para uma posição abaixo, ou seja "self.top.next" significa o elemto abaixo do antigo topo (self.next)
            self._size -= 1
            return node.data
        raise IndexError("Empty stack")
        

    def peek(self):
        #observar e retornar quem é o elemento do topo da pilha, sem o remover
        if self._size>0:
            return self.top.data
        raise IndexError("Empty stack")

    def __len__(self):
        return self.size

    def __repr__(self):
        r =""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
        

    


        

