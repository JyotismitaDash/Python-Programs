l=[10,20,30,40,50,60]
for i in range(len(l)):
    print(i)
    print("")
    if i%2==0:
        print(i)
        l[i],l[i+1]=l[i+1],l[i]
print(l)