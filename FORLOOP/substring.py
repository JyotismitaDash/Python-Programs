#WAP to check how many times the given substring is present in given string
s=input("Enter a string:")
sub=input("Enter sub string:")
c=0
for ip in range(len(s)):
    if s[ip:ip+len(sub):]==sub:
        c=c+1
print(c)
#taking input from user
#taking substing from user
#taking c variable with value zero.bcoz we r assuming that substring might be zero
#let's take a string as hai python
#let's take substing as a pyt
#i-1 :- extracting hai and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-2 :- extracting ai  and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-3 :-extracting i p and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-4 :-extracting  py and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-5 :- extracting pyt and check the condtion , the condition is True so that it will add to c so c becomes 1
#i-6 :-extracting yth and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-7 :- extracting tho and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-8 :-extracting hon and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-9 :-extracting on and check the condtion , the condition is false it will not enter to if block so c becomes 0
#i-10 :-extracting n and check the condtion , the condition is false it will not enter to if block so c becomes 0