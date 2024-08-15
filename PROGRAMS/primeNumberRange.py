ll=int(input("Enter lower limit here:-"))
ul=int(input("Enter upper limit here:-"))
for num in range(ll,ul+1):
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print(num)
    