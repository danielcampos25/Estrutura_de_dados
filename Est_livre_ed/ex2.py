'''objetivo do exercicio é corrigir a funçao de remover um item d e tal
forma que se for inserido um elemento não presente na unordered list o erro seja 
devidamente tratado'''

def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if  current.getNext() == None:
                    break
        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        elif not found:
            return

    
