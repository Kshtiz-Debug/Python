"""
Develop a program that uses Student which prompts the user to enter marks in three subjects
and calculates total marks , percentage , and display the score card details
Use list to store the marks in three subjects and total marks . use __init__() method to initialise
name, Usn and the list to store marks and total. Use getMarks() method to read marks into the list
and display() method to display the score card details.
"""

class Student():
    def __init__(self,name,usn,lis=[]):
        self.lis=lis
        self.name = name
        self.usn = usn

    def getMarks(self):
        mark1=int(input())
        mark2 = int(input())
        mark3 = int(input())
        self.lis[0]=mark1
        self.lis[1] = mark2
        self.lis[2] = mark3






X1=Student(12,23)

