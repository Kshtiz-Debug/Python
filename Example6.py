"""import openpyxl
import sys
N=int(sys.argv[1])
wb=openpyxl.Workbook()
sheet=wb.active
row=1
sheet.title="Multiplication Table"


for i in range(1,N+1):
    for j in range(1,11):
        result=f"{i}*{j}={i*j}"
        sheet.cell(row,column=1,value=result)
        row+=1
wb.save("Multiplication.xslx")
print(f"Multplication table from 1*1 to {N}*10 has been saved to Multiplication.xslx")"""

"""
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


def add_complex_numbers(complex_list):
    result = Complex(0,0)
    for c in complex_list:
        result =result+c
    return result


# Input number of complex numbers
N = int(input("Enter the number of complex numbers (N >= 2): "))
if N<2:
    print("N must be atleast 2")
else:
    complex_numbers = []

# Read N complex numbers
    for i in range(N):
        real = float(input(f"Enter real part of complex number {i + 1}: "))
        imag = float(input(f"Enter imaginary part of complex number {i + 1}: "))
        complex_numbers.append(Complex(real, imag))

# Compute the sum of all complex numbers
result = add_complex_numbers(complex_numbers)

# Display the result
print("The sum of the complex numbers is:", result)\
    
"""

class Student:
    def __init__(self, name="", usn="", score=[0, 0, 0, 0]):
        self.name = name
        self.usn = usn
        self.score = score

    def getMarks(self):
        self.name = input("Enter student Name : ")
        self.usn = input("Enter student USN : ")
        self.score[0] = int(input("Enter marks in Subject 1 : "))
        self.score[1] = int(input("Enter marks in Subject 2 : "))
        self.score[2] = int(input("Enter marks in Subject 3 : "))
        self.score[3] = self.score[0] + self.score[1] + self.score[2]

    def display(self):
        percentage = self.score[3] / 3
        spcstr = "=" * 50
        print(spcstr)
        print("SCORE CARD DETAILS".center(50))
        print(spcstr)
        print("%15s" % ("NAME"), "%12s" % ("USN"), "%8s" % "MARKS1", "%8s" % "MARKS2", "%8s" % "MARKS3",
              "%8s" % "TOTAL", "%12s" % ("PERCENTAGE"))
        print(spcstr)
        print("%15s" % self.name, "%12s" % self.usn, "%8d" % self.score[0], "%8d" % self.score[1],
              "%8d" % self.score[2], "%8d" % self.score[3], "%12.2f" % percentage)
        print(spcstr)


def main():
    s1 = Student()
    s1.getMarks()
    s1.display()


main()
