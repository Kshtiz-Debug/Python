import shelve
x=shelve.open("CODED",'w')
x["message"]="Hello World"
x.close()

print(x)