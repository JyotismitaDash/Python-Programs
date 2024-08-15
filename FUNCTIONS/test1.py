n=input("enter numbers:-")
v='aeiouAEIOU'
s=''
for ip in range(len(n)):
    if n[ip].isalpha() and not n[ip] in v:
        s+=n[ip]
    if n[ip] in v:
        k=ip*100
        sum=0
        for num in range(1,k+1):
            for i in range(2,num//2+1):
                if num%i==0:
                    break
                else:
                    sum+=num
        print(sum)
        
print(s)
                

    


