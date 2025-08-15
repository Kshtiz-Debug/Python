num=input("Enter a number")
print(num)
uniqDig=set(num)
print(uniqDig)
for elem in uniqDig:
    print(elem,"occurs",num.count(elem),"Times")