'''
A B C D E
B D F H J
C F I L O
D H L P T
E J O T Y
'''
n=int(input("Enter n values:-"))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        dummy+=row
    print()