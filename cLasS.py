#
#class---) blueprint of ojects
# objects -----) Instance of class

class person:
    def __init__(self,name,relation,age):
        self.name=name
        self.age = age
        self.relation=relation


    def getName(self):
        return self.name

P1=person("Bob","Uncle",23)
print(P1.getName())