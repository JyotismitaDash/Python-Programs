
pc=0
n=1
while True:
    sum=0
    d=n
    order=len(str(n))
    while d>0:
        rem=d%10
        sum=sum+(rem**order)
        d=d//10
    if sum==n:
        pc=pc+1
        if pc>=6 and pc<=10:
            print(n)
    if pc==10:
        break        
    n=n+1