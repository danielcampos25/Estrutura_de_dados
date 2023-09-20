
lista_exemplo = [23,2,60,40,5,6,13,70]
'''No pior dos casos (lista ordenada inversamente) 
o algoritmo de troca sera executado (n-1) vezes'''


def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):#(n-1) pois não há elemento sucessor para ser comparado com o ultimo elemento da lista
            if lista[i]>lista[i+1]:
                '''Em python é possivel ultilizar o comando abaixo 
                para trocar variaveis sem a necessidade de se criar 
                uma variavel auxiliar'''
                lista[i],lista[i+1] = lista[i+1],lista[i]  
                '''troca de elementos da lista caso o 
                anterior seja maior do que o seu sucessor '''
    return(lista)

print(bubble_sort(lista_exemplo))