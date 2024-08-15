c=int(input("enter:-"))
pc=0
n=1
while True:
    d=n
    sum=0
    while d>0:
        rem=d%10
        sum=sum+rem
        d//=10
    if n%sum==0:
        print(n)
        pc+=1
    if pc==c:
       break
    n=n+1

