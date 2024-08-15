#wap to check program is perfect number or not
n=int(input("Enter a Number:-"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect num")
else:
    print("not a perfect num")
#Taking number from user
#Take one variable as sum with 0 as values bcoz we r assuming the given divisor might be zero
#let's take a number 6
#condition:It will check 1 to 3 .If the number is divisible by 1 to 3 then it will add the divisor to sum then it will check if the number is equl to sum then the number will be Perfect Number otherwise not a perfect number
#iteration 1:iterates 1 and check the condition and add 1 to sum so sum becomes 1
#iteration 2:iterates 2 and check the condition and add 2 to sum so sum becomes 3
#iteration 3:iterates 3 and check the condition and add 3 to sum so sum becomes 6
# sum==n so 6 is a perfect number