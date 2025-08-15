"""

import sys
import os.path

fname=input("Enter the name of the file")
if not os.path.isfile(fname):
    print("The file does not exist")
    os.exit(0)

infile=open(fname,"r")
myList=infile.readlines()
print(myList)
lineList=[]

for line in myList:
    lineList.append(line.strip())
lineList.sort()
outfile=open("Sorted.txt","w")
for line in lineList:
    outfile.write(line+"\n")
infile.close()
outfile.close()
if os.path.isfile("Sorted.txt"):
    print("The sorted file created succesfully")
    print("The sorted file contents are")
    f=open("Sorted.txt","r")
    l=f.readlines()
    for i in l:
        print(i,end="")


"""
import sys
import os.path
fname=input("Enter the name of the file")
if not os.path.isfile("fname"):
    print("The file does not exist")
    sys.exit(0)


infile=open("fname","r")
x=infile.readlines()
lineList=[]
for i in x:
    print(lineList.append(i.strip()))
lineList.sort()


outfile=open("Sorted.txt","w")
for i in lineList():
    outfile.write(i+"\n")
infile.close()
outfile.close()
if os.path.isfile("Sorted.txt"):
    print("The Sorted text file has been created succesfully")
    print("The contents of the sorted file are")
    m=open("Sorted.txt")
    c=m.readlines()
    for n in c:
        print(n,end="")


