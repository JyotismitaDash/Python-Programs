#i/p=[12, 35, 9, 56, 24]-----o/p=[24, 35, 9, 56, 12]
#def swapList(lst):
 #   lst[0],lst[-1]=lst[-1],lst[0]
 #   return lst
#lst=[12, 35, 9, 56, 24]
#print(swapList(lst))

lst=[12, 35, 9, 56, 24]
nl=[lst[-1]]+lst[1:-1]+[lst[0]]
print(nl)