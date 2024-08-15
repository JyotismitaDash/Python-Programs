'''
    A
   BC
  DEF
 GHIJ
KLMNO    
'''
n=int(input("enter n values:"))
dummy=1
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        dummy+=1
    print()
    stars+=1
    spaces-=1