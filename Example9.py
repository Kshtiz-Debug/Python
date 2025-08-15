import csv
fileob=open("Studentdata1.csv")
readerobj=csv.reader(fileob)
next(readerobj)
highestcgpa=0
topperdetails=None

for row in readerobj:
    usn,name,cgpa=row[0],row[1],float(row[2])
    if cgpa>highestcgpa:
        highestcgpa=cgpa
        topperdetails=(usn,name,cgpa)

if topperdetails:
        print(f"topper of the class:\nUSN:{topperdetails[0]},Name:{topperdetails[1]},cgpa:{topperdetails[2]}")
