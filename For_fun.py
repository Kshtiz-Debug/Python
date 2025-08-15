
"""
x=dict(hello="1",he="2")
x.update(Nun="Movie")
print(x)
------------------------------------------------------------------------------------------------


Or

--------------------------------------------------------------------------------------------------
x={"Nun":"1"}
x.update(nUn="movie")  
x.update(Nun="12")
print(x)



#In Python, when using the dict.update() method with keyword arguments, you don't need to use double quotes around the keys. This is because keyword arguments are treated as identifiers, not as strings. The keys are automatically converted to strings by Python.

----------------------------------------------------------------------------------------------------

x={"Nun":"1"}
x.update(nUn="")
print(x)

---------------------------------------------------------------------------------------

string1 = "Hello, world!"
inserted_string = "Python"
new_string = string1.replace("world", inserted_string)
print(new_string)




----------------------------------------------------------------------------------------------




txt = "apple, banana, cherry, pie"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(",", 1)
print(x)
#If you give the value of the maxsplit then the split function will split it in that many pieces.



------------------------------------------------------------------------------------------------------


x=dict(x={1:"2"},y=123,z=12)
print(x.keys())
print(x.values())


for i in x.values():
    print(i)

print(x.items())


---------------------------------------------------------------------------------------------------

class timer:
    def __init__(self,h,m,s,add):
        self.h=h
        self.m=m
        self.s=s
        self.add=add
    def str(self):
        return f"{self.h}:{self.m}:{self.s}"
    def added(self):
        while self.add!=0:
            if self.add <= 60:
                self.s = self.s + self.add
                self.add=self.add-self.add
                if self.s > 60:
                    self.m = self.m + 1
                    self.s = self.s - 60
            while self.add > 60:
                self.m = self.m + 1
                self.add = self.add - 60
                if self.m>60:
                    self.h=self.h+1
                    self.m=self.m-60
        return f"{self.h}:{self.m}:{self.s}"
T1=timer(2,34,24,3662)
print(T1.str())
print(T1.added())


--------------------------------------------------------------------------------------------------

x="Hello World , soon i am gonna rule , it will be my time"
x=x.upper()
print(x)


x=x.split()
print(x)

x=" ".join(x)
print(x)


-------------------------------------------------------------------------------------------------

c='''Bennett University, regarded as one of
the best colleges in India is bestowed with
prestigious awards and honours to recognize the
remarkable contribution made in the field of higher
education in India, successfully moulding young minds into 
becoming skilled professionals.'''




print(c)
c=c.split("r")
print(c)


c="r".join(c)
print(c)

-------------------------------------------------------------------------------------------------------

"""