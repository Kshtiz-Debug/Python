'''print("India's capital is New Delhi.")
print("d")
print("\N{thinking face}")
'''

import random
l=[]
#This program focuses on the list part of the python
print("Tell us how many elements you want in your list")
xx=int(input())
print("Tell us the starting domain for that random list")
yy=int(input())
print("Tell us the ending domain for that random list")
zz=int(input())
for i in range(xx):
    l.append(random.randint(yy,zz))
print(l)

'''
print("Enter the number to be founnd")
x=int(input())


def Finding_a_Number_From_A_List():
    i=0
    while(i<len(l)):
        if(x==l[i]):
            print("The number is found")
            break
        else:
            print("Element not found")
        i=i+1


print("What do you want to perform ")
print("If you want to find a number from a list then press 1")
y=int(input())
if(y==0):
    print("Sorry program crashed")
else:
    print("Okay sir got it")
    Finding_a_Number_From_A_List()

'''



def Find_A_Number():
    print("Enter the number to be found ")
    x=int(input())
    flag=0
    m=0
    for i in l:
        m=m+1
        if(x==i):
            print("The number is found at the position",m)
            flag=1
            break
    if(flag==0):
        print("The number is not present")
print("what do you want to perform here")
print("If you want to find a number then press 1")
v=int(input())
if(v==1):
    Find_A_Number()




