c=int(input("Enter n values:-"))
pc=0
n=1
while True:
    sum=0
    d=n
    while d>0:
        rem=d%10
        d=d//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
            sum=sum+fact
    if sum==n:
        print(n)
        pc+=1
    if c==pc:
        break
    n=n+1

