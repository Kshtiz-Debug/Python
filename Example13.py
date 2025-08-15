class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name},{self.age}"


P1=Person("Ravi",29)
print(P1)