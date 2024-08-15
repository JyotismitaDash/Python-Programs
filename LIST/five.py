list1 = [10, 20, 4, 45, 99]
 
mx = max(list1[0], list1[1]) 
secondmax = min(list1[0], list1[1]) 
n=len(list1)
for i in range (2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and mx!=list1:
        secondmax=list1[i]

print(secondmax)

def second_largest(arr):
    #if len(arr) < 2:
       # return -1

    mx = max(arr[0], arr[1])
    secondmax = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > mx:
            secondmax = mx
            mx = arr[i]
        elif arr[i] > secondmax and mx != arr[i]:
            secondmax = arr[i]

    if mx == secondmax:
        return -1
    else:
        return secondmax

# Test the function
arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr))  # Output: 34

arr = [10, 10]
print(second_largest(arr))  # Output: -1