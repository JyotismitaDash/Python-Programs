def isEven(n):
    if n%2==0:
        return True
    else:
        return False
def evenNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isEven(n):
            print(n)
evenNumbers(10,20)

