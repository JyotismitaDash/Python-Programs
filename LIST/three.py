#Python program to find smallest number in a list
l=[20,30,21,1]
min=l[0]
for i in l:
    if i<min:
        min=i
print(min)