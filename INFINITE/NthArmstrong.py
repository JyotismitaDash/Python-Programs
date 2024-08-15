c=int(input("enter"))
pc=0
n=1
while True:
    sum=0
    order=len(str(n))
    d=n
    while d>0:
        rem=d%10
        sum=sum+(rem**order)
        d=d//10
    if sum==n:
        pc=pc+1
    if pc==c:
        print(n)
        break
    n=n+1

