'''s=input("Enter a sting:-")
rev=""
for ip in range(-1,-(len(s)+1),-1):
    rev=rev+s[ip]
print(rev)


s=input("Enter a sting:-")
rev=""
for ch in s:
    rev=ch+rev
print(rev)


s=input("Enter a sting:-")
rev=''
i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)
'''

s=input("Enter a sting:-")
rev=""
i=-1
while i>-(len(s)+1):
    rev=rev+s[i]
    i=i-1
print(rev)