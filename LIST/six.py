#Python program to find N largest elements from a list
L=[2, 6, 41, 85, 0, 3, 7, 6, 10]
n=int(input("enter nth position"))
final_list=[]
for i in range(n):
    mx=0
    for j in range(len(L)):
        if L[j]>mx:
            mx=L[j]
    L.remove(mx)
    final_list.append(mx)
print(final_list)
