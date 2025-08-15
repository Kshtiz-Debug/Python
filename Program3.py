x=input("Enter the number please:\n")
v=[]
for i in x:
    v.append(i)

print(v)
d={}
for k in v:
    if k not in d:
        d[k]=1
    else:
        d[k]+=1
print(d)