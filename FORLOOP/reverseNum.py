n=int(input("Enter a number:-"))
d=n
rev=0
while d>0:
    rem=d%10
    d=d//10
    rev=rev*10+rem
print(rev)