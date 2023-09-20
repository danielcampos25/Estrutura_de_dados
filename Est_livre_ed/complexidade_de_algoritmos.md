#Complexidade de Algoritmos (revisão)
-Medir a quantidade de recursos demandados na implementação de um determinado algoritmo, podendo ser de tempo, espaço na memoria etc.
exemplo: inverter termos de uma dada lista com dados

def inverter_lista(lista):
    tamanho = len(lista)
    limite = tamanho//2      #pega metade da lista
    for i in range(limite):
        aux = lista[i]
        lista[i]=lista [n-1]
        lista[tamanho-i] = aux


def inverter_lista2(lista):
    nova_lista = []
    tamanho = len(lista)
    for i in range(tamanho):
        nova_lista.append(lista[tamanho-i])
    return nova_lista


-Notação "Big O":
