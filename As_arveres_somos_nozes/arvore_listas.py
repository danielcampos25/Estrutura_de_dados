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
    '''Função inorder:
    1) Nó esquerda
    2)Nó raíz
    3)Nó direita


    '''
    def read_inorder(self):
        self._read_inorder(self.tree)

    def _read_inorder(self, subtree):
        if subtree:
            left, root, right = subtree
            self._read_inorder(left)
            print(root, end=' ')  # Imprime o elemento do nó raiz
            self._read_inorder(right)
    ''' Leitura pós ordem:
    1)Nó esquerda
    2)Nó direita
    3) Nó raiz
    '''
    def postorder(self):
        return self._postorder(self.tree)

    def _postorder(self, subtree):
        if subtree:
            left, root, right = subtree
            return self._postorder(left) + self._postorder(right) + [root]
        return []

    ''' Leitura pré ordem:
    1) Nó raíz
    2) Nó esquerda
    3) Nó direita
    '''
    def preorder(self):
        return self._preorder(self.tree)

    def _preorder(self, subtree):
        if subtree:
            left, root, right = subtree
            return [root] + self._preorder(left) + self._preorder(right)
        return []


