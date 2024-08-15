#WAP to find the sum of index position of substring in a given string
S=input("Enter string:-")
Sub=input("Enter substring:-")
sum=0
for ip in range(len(S)):
    if S[ip:ip+len(Sub):]==Sub:
        sum=sum+ip
print(sum)

# Taking string from user
# Taking substring from user
# Take one variable as sum with 0 as values bcoz we r assuming that the given substring might be zero
#Let's take a string as a hai python
#Let's take a substring as a py
#i-1:- extracting ha and check the condition , the condition is false it will not enter to if block so sum becomes 0 
# i-2:- extracting ai and check the condition , the condition is false it will not enter to if block so sum becomes 0
#i-3:- extracting i  and check the condition , the condition is false it will not enter to if block so sum becomes 0
#i-4:- extracting  p and check the condition , the condition is false it will not enter to if block so sum becomes 0
#i-5:- extracting  py and check the condition , the condition is True it will  enter to if block so ip[4] will add to sum so sum becomes 4
#i-6:-extracting  yt and check the condition , the condition is false it will not enter to if block so sum becomes 4 
#i-7:- extracting th and check the condition , the condition is false it will not enter to if block so sum becomes 4
#i-8:-extracting ho and check the condition , the condition is false it will not enter to if block so sum becomes 4
#i-9:-extracting  on and check the condition , the condition is false it will not enter to if block so sum becomes 4
#i-10:-extracting  n and check the condition , the condition is false it will not enter to if block so sum becomes 4