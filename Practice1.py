"""import os
print(os.path.join("Users","str"))


"""


import os.path
import sys
fname=input("Enter file name whose contents are to be sorted ")
if not os.path.isfile(fname):
    print(fname,"Does not exist")
    sys.exit(0)


infile=open(fname,"r")
myList=infile.readlines()
print(myList)
lineList=[]
for line in myList:
    lineList.append(line.strip())
lineList.sort()
outfile=open("sorted.txt","w")
for line in lineList:
    outfile.write(line+"\n")
infile.close()
outfile.close()
if os.path.isfile('sorted.txt'):
    print("\nFile containing sorted contents sorted.txt created successfully")
    print("Contents of sorted text")
    print("===================================================================")
    rdfile=open("sorted.txt","r")
    for line in rdfile:
        print(line,end="")

"""
import os.path
import sys
fname=input("Enter the file name:")
if not os.path.isfile("fname"):
    print("The file does not exist")
    sys.exit(0)

infile=open("fname","r")
myList=infile.readlines()
print(myList)

"""