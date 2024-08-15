#WAP to print reverse number
n=int(input("Enter a number:-"))
d=n
rev=0
while d>0:
    r=d%10
    rev=rev*10+r
    d=d//10
if rev==n:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not a palindrome")
