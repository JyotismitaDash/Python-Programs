n=int(input("Enter n values:-"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n," is not a prime number")
            break
    else:
        print(n," is a Prime number")
else:
    print(n,"not a prime number")