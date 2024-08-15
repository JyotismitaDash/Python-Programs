'''A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y'''
n=int(input("enter number"))
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=" ")
        dummy+=n
    print()