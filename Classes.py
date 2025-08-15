class Engineer:
    def __init__(self,age,level,name="",position=""):
        self.name=name
        self.age=age
        self.position=position
        self.level=level

S1=Engineer(41,'Beginner',"Ramu","Video Editor")


class Doctor:
    def __init__(self,age,level,name="",position=""):
        self.name=name
        self.age=age
        self.position=position
        self.level=level

D1=Doctor(21,3,'ruhi',"Surgeon")
print(D1.position)