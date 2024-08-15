n=int(input("enter a number:"))
d=n
sum=0
while d>0:
    rem=d%10
    sum=sum+rem
    d=d//10
print(f'sum of {n} is {sum}')