#wap to check how many elements are present in a given sting
n=int(input("Enter a Number:-"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
#Taking number from user
#Take one variable as sum with 0 as values bcoz we r assuming the given number might be zero
# let's take a num is 3
#iteration 1:iterates 1 and add 1 to sum so sum becomes 1
#iteration 2:iterates 2 and add 2 to sum so sum becomes 3
#iteration 3:iterates 3 and add 3 to sum so sum becomes 6