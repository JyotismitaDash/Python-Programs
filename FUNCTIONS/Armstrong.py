def isArmstrong(n):
    d=n
    order=len(str(n))
    sum=0
    while d>0:
        rem=d%10
        d=d//10
        a=rem**order
        sum=sum+a
    if n==sum:
        return True
    else:
        return False
isArmstrong(153)