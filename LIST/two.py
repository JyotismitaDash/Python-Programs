#swap two elements in list
#i/p=[23,65,19,90]pos1=1,pos2=3----o/p=[19,65,23,90]
def swapList(lst,pos1,pos2):
    lst[pos1],lst[pos2]=lst[pos2],lst[pos1]
    return lst
lst=[23,65,19,90]
pos1=1
pos2=3
print(swapList(lst,pos1-1,pos2-1))