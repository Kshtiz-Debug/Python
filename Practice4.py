dict={}
n=int(input("Enter the number of values u want to enter"))
for i in range(n):
    name=input("Enter name of th person")
    number=input("Enter the number")
    dict[name]=number
print(dict)

dict["Welp"]="134"
print(dict)


del dict["Welp"]
print(dict)