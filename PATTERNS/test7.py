'''
        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
'''
n=int(input('Ener n values:-'))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        dummy+=1
    print()
    spaces-=1
    stars+=2
