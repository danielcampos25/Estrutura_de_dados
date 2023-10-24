def merge(l1,l2):
    for i in range(len(l2)):
        l1.append(l2[i])

    for j in range(len(l1)-1,0,-1):
        for i in range(j):
            if l1[i+1]<l1[i]:
                l1[i+1],l1[i] = l1[i],l1[i+1]
        
    return l1 

'''Questão da P1 de ED que pedia para criar uma função que recebia duas listas ja ordenadas e
retornavs uma lista também ja ordenada resultante da junção entre as duas. Foi usado o bubble 
sort e a entrada pode ser qualquer lista, não precisa estar ordenada, o resultado será uma lista ordenada
'''