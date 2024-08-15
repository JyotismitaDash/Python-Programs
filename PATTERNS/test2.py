''' A
    BB
    CCC
    DDDD
    EEEEE

    '''
n=int(input("enter n values:"))
dummy=1
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
    print()
    dummy+=1
    stars+=1