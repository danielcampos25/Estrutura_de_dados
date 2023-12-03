class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def mostra(node):
    print('(', end = '')
    if node:
        print(f'{node.data}', end = '')
        mostra(node.left)
        print('',end='')
        mostra(node.right)
    print(')', end = '')

#Implementar: deve chamar a função 'mostra' para imprimir todas as subarvores cujas raizes se encontram no nivel fornecido como parametro

def mostra_nivel(raiz,nivel):
    if raiz is not None and nivel == 0:
        mostra(raiz)
        print()
    if raiz:
        mostra_nivel(raiz.left,nivel-1)
        mostra_nivel(raiz.right,nivel-1)