class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class Deck:
    def __init__(self):
        self._size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self._size==0

    def add_front(self,elem):
        node = Node(elem)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.front.previous = node
            node.next = self.front
            self.front = node

        self._size+=1
            

    def add_rear(self,elem):
        node = Node(elem)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            node.previous = self.rear
            self.rear = node

        self._size +=1



    def remove_front(self):
        if not self.is_empty():
            if self.front.next:
                self.front = self.front.next
                self.front.previous = None
            else:
                self.front = None
                self.rear = None
            self._size -=1

    def remove_rear(self):
        if not self.is_empty():
            if self.rear.previous:
                self.rear = self.rear.previous
                self.rear.next = None
            else:
                self.front = None
                self.rear = None
            self._size -= 1

    def size(self):
        return self._size


def exibe_candidatos(deque,pos,ordem):
    if ordem == 'direta':
        pointer = deque.front
        for i in range(pos):
            pointer = pointer.next
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next


    elif ordem =='inversa':
        pointer = deque.rear
        for i in range(pos):
            pointer = pointer.previous
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next

