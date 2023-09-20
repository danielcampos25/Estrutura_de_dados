n = int(input())

def remove_repeated(string):
    new_string = ""
    for element in string:
        if element not in new_string:
            new_string+=element
    return new_string

for i in range(n):
    cronogram = list(input())
    a= list(input())
    b= list(input())
    c= list(input())
    total = a+b+c
    failed = False
    for element in total:
        if element in cronogram:
            cronogram.remove(element)
        else:
            print("You died!")
            failed = True
            break
    if failed == False:
        cronogram = remove_repeated(cronogram)
        if len(cronogram)!=0:
            ans =''.join(sorted(cronogram))
            print(f'Bora ralar: {ans}')
        else:
            print("It's in the box!")


        
