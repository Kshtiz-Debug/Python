class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def add(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)

    def __str__(self):
        return f"{self.real}+{self.imag}i"


c1=Complex(1,2)
c2=Complex(10,5)


x=Complex.add(c1,c2)
print(x)