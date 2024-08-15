def equilibrium(arr):
    n = len(arr)
    for i in range(n):
        left_sum=arr[:i]
        right_sum=arr[i+1:]
        if left_sum == right_sum:
            return i+1
    return -1
# Test the function
print(equilibrium([1, 2, 3, 4, 3,]))

def equilibrium(arr):
    total_sum=sum(arr)
    left_sum=0
    n = len(arr)
    for i in range(n):
        total_sum-=arr[i]
        if total_sum==left_sum:
            return i+1
        left_sum+=arr[i]
    return -1
print(equilibrium([1, 3, 5, 2, 2]))
