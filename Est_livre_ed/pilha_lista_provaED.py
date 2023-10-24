'''O objetivo do exercicio da prova era implementar uma pilha usando a classe ja 
existente de fila e seus métodos, push, pop ...
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None

    def isEmpty(self):
        return self._size == 0

    def size(self):
        return self._size

    def push(self,elem):
        node = Node(elem)
        if self.isEmpty():
            self.first = node
            
        elif self.last is None:
            self.first.next = node
            self.last = node

        else:
            self.last.next = node
            self.last = node

        self._size +=1

    def pop(self):
        if self.isEmpty():
            return ("lista vazia")
        elif self._size ==1 :
            elem = self.first
            self.first = None
            self._size -=1
            return elem
            
        elif self._size ==2:
            elem = self.first
            self.first = self.last
            self.last = None
            self._size -=1
            return elem
        elif self._size > 2:
            elem = self.first
            self.first = self.first.next
            self._size -=1

            return elem
    def remove(self, elem):
        if self.isEmpty():
            return "Lista vazia"

        previous = None
        current = self.first

        while current is not None:
            if current.data == elem:
                if previous is None:
                    # O elemento a ser removido está no primeiro nó
                    self.first = current.next
                else:
                    # O elemento a ser removido está em algum lugar no meio ou no final da fila
                    previous.next = current.next

                if current == self.last:
                    # Se o elemento a ser removido for o último, atualize self.last
                    self.last = previous

                self._size -= 1
                current = current.next
            else:
                previous = current
                current = current.next

    def print(self):
        if self.isEmpty() is not True:
            pointer = self.first
            fila = ''
            while pointer:
                fila+= str(pointer.data) + '-'
                pointer = pointer.next
            print(fila)
        else:
            print('Fila vazia')



class Stack:
    def __init__(self):
        self.f = Queue()
        self.first = None
        self.last = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0 

    def size(self):
        return self._size

    def push(self,elem):
        
        self.f.push(elem)

        self._size +=1

    def print1(self): #por que nao ta funcionando!??
        
        if self.isEmpty():
            return("pilha vazia")
        elif self._size > 1:
            aux2 = Queue()
            while self.f.isEmpty() is not True:
                pointer = self.f.first
                
                while pointer is not self.f.last:
                    pointer = pointer.next
                aux2.push(pointer.data)
                self.f.remove(pointer.data)
            aux2.print()

        elif self.f._size ==1:
            self.f.print()


    def print2(self):
        if self.isEmpty():
            return("pilha vazia")
        elif self._size > 1:
            aux2 = Queue()
            while self.f.isEmpty() is not True:
                pointer = self.f.first
                
                while pointer is not self.f.last:
                    pointer = pointer.next
                aux2.push(pointer.data)
                self.f.remove(pointer.data)
            aux2.print()

        elif self.f._size ==1:
            self.f.print()





pilha = Stack()
pilha.push("A")
pilha.push("B")
pilha.push("C")
pilha.push("D")
pilha.push("E")
pilha.push("F")
pilha.print1()
pilha.print2()


        

