def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
        

def sumOfNumber(num):
    sum=0
    for num in range(2,num+1):
        if isPrime(num):
            sum+=num
            
