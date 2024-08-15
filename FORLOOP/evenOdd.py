#l=[10,21,6]
#[even,odd,even]
l=eval(input("Enter  String:-"))
nl=[]
for ip in range(len(l)):
    if l[ip]%2==0:
        nl.append('even')
    else:
        nl.append('odd')
print(nl)