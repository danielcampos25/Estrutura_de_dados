'''
pop() - remove e retorna o ultimo item da lista
pop(pos) - remove e retorna o itme selecionado
'''
#Implementando listas ligadas:
class Node:    #Nós são componentes de listas que se encadeiam entre si, são compostos pelo dado e pelo seu "indicador de próximo"
    def __init__(self,initData): #função construtora do nó
        self.data = initData    
        self.next = None
    #relações
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData
    
    def setNext(self,newNext):
        self.next = newNext

class UnorderedList:
    def __init__(self) -> None:
        pass
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current!= None:
            count +=1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current!= None and not found:
            if current.getData()==item:
                found = True
            else:
                current=current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData()==item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
