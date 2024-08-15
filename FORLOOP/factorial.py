#wap to find factorial of a given number
n=int(input("Enter a Number:-"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
#Taking a number from user
#Take one variable as fact with 1 as values bcoz we r assuming the given number might be zero so 0's factorial is 1
# let's take a num is 3
#iteration 1:iterates 1 and multiply 1 to fact so fact becomes 1
#iteration 2:iterates 2 and multiply 2 to fact so fact becomes 2
#iteration 3:iterates 3 and multiply 3 to fact so fact becomes 6