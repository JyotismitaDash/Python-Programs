'''
ABCDE
FEDC
BCD
EF
C
'''
n=int(input("Enter n values:-"))
dummy=1
stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    stars-=1
