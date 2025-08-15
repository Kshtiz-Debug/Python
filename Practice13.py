s="IX"
l=[]
sum=0
for char in s:
    l.append(char)
print(l)
dict={"I":1,"V":5,"X":10}


for k in range(len(l)-1):
    if dict[l[k]]>=dict[l[k+1]]:
        sum = sum + dict[l[k]]
    else:
        sum=sum-dict[l[k]]
sum=sum+dict[l[len(l)-1]]
print(sum)
