'''
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
'''
n=5
star=1
#dummy=n
for row in range(1,n+1):
    dummy=n-row+1
    for st in range(1,star+1):
        print(dummy,end=' ')
        dummy+=1
        
    print()
    star+=1
