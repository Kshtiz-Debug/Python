x=int(input("Enter the value of the first variable"))
y=int(input("Enter the value of the second variable"))
print("What do you want to implement on both variables")
z=int(input("1 for Addition\n2 for subtraction\n-"))
if(z==1):
    def Add():
        print("Okay, your final result is:")
        return x+y
print(Add())
