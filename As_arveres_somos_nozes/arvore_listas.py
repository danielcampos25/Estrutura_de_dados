#implementando arvore usando listas python

class BinaryTree:
    def __init__(self,root = None):
        if root is None:
            root = []
        else:
            self.tree = [root, [],[]]

    def insert_left(self,elem):
        if len(self.tree)>1:
            subtree = self.tree.pop(1)
            if len(subtree)>0:
                self.tree.insert(1,[elem,subtree,[]])
            else:
                self.tree.insert(1,[elem,[],[]])
        else:
            self.tree.insert(1,[elem,[],[]])

    def insert_right(self,elem):
        if len(self.tree)>2:
            subtree = self.tree.pop(2)
            if len(subtree)>0:
                self.tree.insert(2,[elem,[],subtree])
            else:
                self.tree.insert(2,[elem,[],[]])

    def _inorder(self,subtree):
        if subtree:
            return (self._inorder)