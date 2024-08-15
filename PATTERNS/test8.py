'''
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
'''
n=int(input("Enter n values:"))
spaces=n-1
stars=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=" ")
        if st<=stars//2:
            dummy+=1
        else:
            dummy-=1
    print()
    stars+=2
    spaces-=1