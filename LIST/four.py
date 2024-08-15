#Python program to find largest number in a list
l=[30,10,100,9]
mx=0
for i in l:
    if mx<i:
        mx=i
print(mx)