list=[]
num=int(input("Enter the number of elements you want to add"))
for i in range(num):
    print("Enter the number you want to add to your list")
    n=int(input())
    list.append(n)
print("The length of your list is:",len(list))
print("The contents of the list r ",list)


total=0
for i in list:
    total=total+i
print("The sum of all the valus of your list is ",total)
mean=total/num
print("The mean of the elements in your list is",mean)


y=0
for i in list:
    x=(i-mean)**2
    y=y+x


variance=y/(num)
print("The variance of the elements in the list is",variance)


stDt=variance**0.5
print(stDt)