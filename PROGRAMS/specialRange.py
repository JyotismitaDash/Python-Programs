ll=int(input("enter lower limit here:"))
ul=int(input("enter upper limit here:"))
for num in range(ll,ul+1):
    d=num
    sum=0
    while d>0:
        rem=d%10
        d=d//10
        fact=1
        for i in range(1,rem+1):
            fact=fact*i
        sum=sum+fact
    if sum==num:
        print(num)
