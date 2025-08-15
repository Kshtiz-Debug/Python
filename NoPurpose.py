"""
s=[]

while True:
 print("ENTER THE OPERATION U WANT TO Do")
 print("1.PUSH\n2.POP\n3.DISPLAY\n4.exit")
 choice = int(input("Enter your choice: "))
 if choice==1:
     ele=int(input("Enter the element u want to add:"))
     s.append(ele)
     print(s)
 if choice==2:
     if s==[]:
         print("STACK UNDERFLOW")
     else:
         print("THE POPED OUT ELEMENT IS:",s.pop())
         print("NOW the stack looks like this",s)
 if choice==3:
     print(s)
 if choice==4:
     exit()
"""
"""
def String_func():
    str=input("Enter the string")
    l=str.split(" ")
    if l=='P%':
        print(l)
String_func()

# Next program
def is_leap(year):
    leap = False

    if year % 4 == 0 and year >= 1900 and year <= 100000:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))


"""






























'''

x=" . ".join(["hello","Hi","Bye"])       #This is the use of .join() method

print(x)

'''





x="Hello my name , is prakhar and , i like to play football, What are ur , hobies".split(",")
print(x)








print(help("Module"))