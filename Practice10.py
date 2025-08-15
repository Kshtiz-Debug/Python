high=input("Enter the high end")
low=input("Enter the low end")
flag=0
for x in range(int(low),int(high)+1):
    l = len(str(x))
    z = []
    if l % 2 != 0:
        continue
    else:
        y = int(x)

        for i in range(1, l + 1):
            z.append(y % 10)
            y = y // 10
    sum , b = 0 , 0
    for i in z:
        sum = sum + i
    for j in range(int(l / 2)):
        b = b + z[j]
    if sum - b == b:
        print(x)
        flag=flag+1
    else:
        continue
print(flag)





