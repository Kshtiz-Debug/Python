str=("intelligence")
x=[]
y=[]
z=[]
for i in range(0,len(str),4):
    x.append(str[i])

for i in range(1,len(str),2):
    y.append(str[i])

for i in range(2,len(str),4):
    z.append(str[i])

c=x+y+z
print(c)

for j in range(len(c)):
    if j%2!=0:
        c[j]=c[j].lower()
        print(c[j],end="")

    else:
        c[j]=c[j].upper()
        print(c[j],end="")


