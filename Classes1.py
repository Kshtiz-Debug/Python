"""
class People:
    def __init__(self,name,age,hobby,home,number,level,aura):
        self.name=name
        self.age=age


F1=People("Wookie",56,"Football","India",12,56,100)
print(F1.aura)
"""



class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduceSelf(self):
        return f"The name of the robot is {self.name}"


r1=Robot("Sofhia","White",45)
r2=Robot("David","Blue",68)

print(r1.introduceSelf())
print(r1.name)

print(r1.weight)

print(r2.weight)
"""
Classes are like - Registers:
U remember when you guys were in school , that time teachers used to call all of your names and ask for attendance
So she used register for that thing. Now we all know that info abt us was stored in the schools registers.
It was for every student.
Seperate
Class is like a register or the system of our school that had our info 
like : Parents detail,phone numbers,name,home, village.
So classes are just like that 
Has seperate places where it stores info abt every object of that particular class.
So here the objects are the students .
It simply stores info abt the objects ....

"""