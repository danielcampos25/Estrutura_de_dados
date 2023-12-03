Arvore balanceada: a diferença de altura de qualquer subarvore de um nó seja no maximo 1
                        a
                      /   \
                      b    c
                    /  \  / \
                   e    f g  h
                  /
                 h
Metodos para balancear uma arvore binaria desbalanceada:
1)Destruir a arvore e formar um vetor ordenado percorrendo a arvore em ordem
2)Ir no elemento central do vetor, ele será a raiz, menores a esquerda e maiores a direita
3) Aplicar o metodo anterior recursivamente