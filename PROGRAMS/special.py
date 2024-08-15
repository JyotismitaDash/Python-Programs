n=int(input("Enter number:-"))
sum=0
d=n
while d>0:
    r=d%10
    d=d//10
    fact=1
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
if sum==n:
    print(n,"is a special number")
else:
    print(n,"not a special number")