s=input("enter string:-")
ns=""
v='AEIOUaeiou'
for ip in range(len(s)):
    if s[ip] in v:
        ns=ns+str(ip)
    else:
        ns=ns+s[ip]
print(ns)
