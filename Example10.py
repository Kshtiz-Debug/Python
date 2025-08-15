class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        return Complex(self.real+other.real,self.imag+other.imag)
    def __str__(self):
        return f"{self.real}+{self.imag}i"

def add_complex_numbers(complex_list):
    result=Complex(0,0)
    for c in complex_list:
        result=result+c
    return result

N=int(input("Enter the number of inputs(n>=2)"))
if N<2:
    print("N should be atleast 2")
else:
    Complex_list=[]
    for i in range(N):
        real=float(input(f"Enter the real part{i+1}"))
        imag=float(input(f"Enter the i part{i+1}"))
        Complex_list.append(Complex(real,imag))

result=add_complex_numbers(Complex_list)
print(result)
