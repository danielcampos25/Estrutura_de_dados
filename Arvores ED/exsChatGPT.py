'''
Altura da Árvore: OK

Escreva uma função para calcular a altura de uma árvore binária.
Verificação de Simetria:     OK

Implemente uma função que verifica se uma árvore binária é simétrica.
Contagem de Folhas:        OK

Crie uma função que conta o número de folhas em uma árvore binária (nós sem filhos).
Percurso em Ordem:       OK

Implemente uma função para percorrer uma árvore binária em ordem.
Busca na Árvore:

Escreva uma função de busca para encontrar um valor específico em uma árvore binária.
Remoção de Nós:

Desenvolva uma função para remover um nó específico de uma árvore binária.
Nível Mínimo:

Crie uma função para encontrar o nível mínimo em uma árvore binária (nível da folha mais próxima da raiz).
Soma dos Nós:

Implemente uma função que calcula a soma de todos os nós em uma árvore binária.
Largura da Árvore:

Escreva uma função para calcular a largura de uma árvore binária (número máximo de nós em qualquer nível).
Árvore de Busca Binária (BST):

Construa uma árvore de busca binária a partir de uma lista de valores.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#1)
def alturaBT(AB):
    if AB is None:
        return 0
    hleft = 0
    hright = 0
    if AB.left:
        hleft = alturaBT(AB.left)
    if AB.right:
        hright = alturaBT(AB.right)
    if hleft>hright:
        return hleft+1
    if hright>hleft:
        return hright+1
    
#2)
def verifica_simetria(node):
    abesq = node.left
    abdir = node.right
    def ver_subs(esq,dir):
        if esq is not None and dir is not None:
            if esq.data == dir.data and ver_subs(esq.left,dir.right) and ver_subs(esq.right,dir.left):
                return True
            else:
                return False
        else:
            return False

#3)
def conta_folhas(node,folhas = 0):
    if node is None:
        return 0
    if node.left:
        folhas = conta_folhas(node.left,folhas)
    if node.right:
        folhas = conta_folhas(node.right,folhas)
    if node.right is None and node.left is None:
        folhas+=1
    return folhas


#4)
def inorder_traversal(node):
    if node is None:
        pass
    else:
    
        if node.left:
            inorder_traversal(node.left)
        print(node.data)
        if node.right:
            inorder_traversal(node.right)