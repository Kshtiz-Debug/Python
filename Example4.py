import sys
import os.path
import string
fname=input("Enter the file name")
if not os.path.isfile(fname):
    print("The file does not exist")
    sys.exit(0)

infile=open(fname,"r")
fileElem=" "

for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            fileElem=fileElem+ch
        else:
            fileElem=fileElem+" "


wordFreq={}
wordList=fileElem.split()

for word in wordList:
    if word in wordFreq.keys():
        wordFreq[word]+=1
    else:
        wordFreq[word]=1

"""

sortedWordFreq=sorted(wordFreq.items(),key=lambda x:x[1],reverse=True)



print("=============================================================")
print("10 most frequently occuring words and their count is")


for i in range(10):
    print(wordFreq[i][0],"occurs",wordFreq[i][1],"times")



"""


print(wordFreq.keys()," occured",wordFreq.values(),"times")