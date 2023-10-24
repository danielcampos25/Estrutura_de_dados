class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class Deck:
    def __init__(self):
        self.right = None
        self.left = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0 

    def pushright(self,elem):
        node = Node(elem)
        if self.isEmpty():
            self.right = node
            self.left = node

        else:
            self.right.next = node
            node.previous = self.right
            self.right = node

        self._size +=1


        

    def pushleft(self,elem):
        node = Node(elem)
        if self.isEmpty():
            self.left = node
            self.right = node
        else:
            self.left.previous = node
            node.next = self.left
            self.left = node
        self._size +=1

    def popright(self):
        if self.isEmpty():
            return None
        else:
            print(self.right.data)
            if self.right.previous:
                self.right = self.right.previous
                self.right.next = None
            else:
                self.right = None
                self.left = None

        self._size-=1


    def popleft(self):
        if self.isEmpty():
            return None
        else:
            print(self.left.data)
            if self.left.next:
                self.left = self.left.next
                self.left.previous = None
            else:
                self.left = None
                self.right = None

        self._size-=1

    def print(self):
        if self.isEmpty():
            return ""
        else:
            pointer = self.left
            while pointer:
                print(pointer.data)
                pointer = pointer.next
vals = [0,0]

deque = Deck()
while vals[0] != 'X':
    vals = input().split()
    if len(vals)==1:
        if vals[0]=="P":
            deque.popright()
        elif vals[0]=="D":
            deque.popleft()

    else:
        if vals[0]=="I":
            deque.pushleft(vals[1])
        elif vals[0]=="F":
            deque.pushright(vals[1])
deque.print()

        

