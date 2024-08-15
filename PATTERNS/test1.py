n=int(input("enter n values:"))
stars=1
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        dummy+=1
    print()
    stars+=1
