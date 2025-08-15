class Dog:
    x=3
    def __init__(self,name,age):
        self.age=age
        self.name=name

    def change(self):
        self.age+=1


    def vol(self):
        Dog.x=9

#This change is a instance method-(Have self as a parameter)
F1=Dog("Harish",20)
print(F1.age)
#So Here the F1 is the instance attribute
F1.change()
print(F1.age)

F2=Dog("Django",10)


print(F2.name)


print(F1.x)
print(F2.x)
F1.vol()
print(F1.x)
print(F2.x)




