number=4
y=f"{number:b}"
print("The binary of number is=",y)

z=[]

for i in range(1,number+1):
    z.append(f"{i:b}")
print("The list of binary is :",z)

count=0
for i in z:
    print("the binary number is= ",i)
    for j in i:
        print(j)
        if j=='1':
            count+=1
print("count=",count)
