c=int(input("enter "))
n=1
pc=0
while True:
    sum=0
    order=len(str(n))
    d=n
    while d>0:
        rem=d%10
        sum=sum+(rem**order)
        d=d//10
        
    if sum==n:
        print(n)   
        pc+=1
    if pc==c:
        break
    n=n+1
        



