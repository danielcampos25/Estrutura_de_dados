#outro exemplo de implementação do quick sort

#Primeiro passo: deve-se escolher um elemento pivô
'''
Baseado no valor do elemento pivô deve se separar o restante do array em duas partes
uma com elementos maiores e outra com os elementos menores que o pivô,
Após isso, deve-se implementar a mesma lógica recursivamente para as sublistas
criadas(da esquerda e da direita)
'''

def quick_sort(alist):
    length = len(alist)
    if length<=1:
        return alist
    else:
        pivot = alist.pop()

    items_greater = []
    items_lower = []
    for item in alist:
        if item>pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower)+ [pivot] + quick_sort(items_greater)


#Obs: pior dos casos O(n^2)
#O(n*log(n)) melhor e caso medio