p={'p':2,'k':4,'u':9,'c':2}
d={}
for k,v in p.items():
    if v in d:
        d[v].append(k)
    else:
        d[v]=[k]
print(d)
