#special number (145=1!+4!+5!)
n=int(input("Enter a number:-"))
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
    print(f"{n} is a special number")

else:
     print(f"{n} is not a special number")

