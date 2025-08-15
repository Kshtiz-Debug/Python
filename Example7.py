class Student:
    def __init__(self,name="",usn="",score=[0,0,0,0]):
        self.name=name
        self.usn=usn
        self.score=score


    def getMarks(self):
        self.name=input("Enter the name of the student")
        self.usn=input("Enter the usn of the student")
        self.score[0]=int(input("marks1"))
        self.score[1] = int(input("marks2"))
        self.score[2] = int(input("marks3"))
        self.score[3] = self.score[0]+self.score[2]+self.score[1]

    def display(self):
        percetage=self.score[3]/3
        spcstr="="*45
        print(spcstr)
        print("Student details")
        print(spcstr)
        print("%15s"%("Name"),"%12s"%("USN"),"%8s"%("Marks1"),"%8s"%("Marks2"),"%8s"%("Marks3"))
        print(spcstr)
        print("%15s"%(self.name),"%12s"%self.usn,"%8s"%self.score[0],"%8s"%self.score[1],"%8s"%self.score[2])
        print("Total marks:",self.score[3])


def main():
    class Student:
        def __init__(self, name="", usn="", score=[0, 0, 0, 0]):
            self.name = name
            self.usn = usn
            self.score = score

        def getMarks(self):
            self.name = input("Enter the name of the student")
            self.usn = input("Enter the usn of the student")
            self.score[0] = int(input("marks1"))
            self.score[1] = int(input("marks2"))
            self.score[2] = int(input("marks3"))
            self.score[3] = self.score[0] + self.score[2] + self.score[1]

        def display(self):
            percetage = self.score[3] / 3
            spcstr = "=" * 45
            print(spcstr)
            print("Student details")
            print(spcstr)
            print("%15s" % ("Name"), "%12s" % ("USN"), "%8s" % ("Marks1"), "%8s" % ("Marks2"), "%8s" % ("Marks3"))
            print(spcstr)
            print("%15s" % (self.name), "%12s" % self.usn, "%8s" % self.score[0], "%8s" % self.score[1],
                  "%8s" % self.score[2])
            print("Total marks:", self.score[3])

def main():
    S1 = Student()
    S1.getMarks()
    S1.display()


main()


