def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
             return True
def primeNumbers(ll,ul):
    for num in range(ll,ul+1):
        if isPrime(num):
            print(num)
primeNumbers(1,20)

                    
    