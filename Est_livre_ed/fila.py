class Node:
    def __init__(self,dataInit):
        self.data = dataInit
        self.next = None

class Queue:
    def __init__(self) -> None:
        self._size = 0
        self.first = None
        self.last = None

    def push(self,elem):
        node = Node(elem)
        if not self.last:
            self.last = node
        self.last.next = node
        self.last = node
        if not self.first:
            self.first = node

        self._size+=1

    def pop(self):
        pass

    def peek(self):
        pass

    def __len__(self):
        return self._size
    
