
pc=0
n=1
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc=pc+1
            if pc>=6 and pc<=10:
                print(n) 
    if pc==10:
        break
    n=n+1