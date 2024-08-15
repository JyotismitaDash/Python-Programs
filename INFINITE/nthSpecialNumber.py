n=int(input("Enter N values:"))
num=1
c=0
while True:
    sum=0
    d=num
    while d>0:
        rem=d%10
        d=d//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
    if sum==num:
        c=c+1
    if c==n:
        print(num)
        break
    num+=1