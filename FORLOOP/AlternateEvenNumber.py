LL=int(input("Enter lower limit:"))
UL=int(input("Enter upper limit:"))
l=[]
for i in range(LL,UL+1):
    if i%2==0:
        l.append(i)
print(l[::2])

#Taking LowerLimit & Upper limit from user
#taking l variable with empty list to store even numbers
#range is 1 to 6
#i-1: extract 1 and check the condition the condition is false it's not store in l
#i-2 extract 2 and check the condition the condition is True it's  store the value in l
#i-3: extract 3 and check the condition the condition is false it's not store in l
#i-4 extract 4 and check the condition the condition is True it's  store the value in l
#i-5: extract 5 and check the condition the condition is false it's not store in l
#i-6 extract 6 and check the condition the condition is True it's  store the value in l
#2,4,6 are store inside l
#it will display [2,6] coz we r providing slicing with 2 updation


LL=int(input("Enter lower limit:"))
UL=int(input("Enter upper limit:"))
C=0
for i in range(LL,UL+1):
    if i%2==0:
        C=C+1
        if C%2!=0:
            print(i)


#Taking LowerLimit & Upper limit from user
#Take one variable as C with 0 as values
#range is 1 to 6
#if the condition is true then it will add to C and again check the condition if the condition is true it will print

#i-1 