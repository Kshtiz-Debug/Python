string="a"
dictionary={}
for i in range(26):
    dictionary[string]=ord(string)
    string=chr(ord(string)+1)

"""............................................................................................."""

x=4
strg="uv"
print(strg)
c=[]
for j in strg:
    y = dictionary[j]
    for i in range(x):
        j = j + chr(y + 1)
        y = y + 1
    m = []
    for i in range(x):
        m.append(j[i + 1])
    answer = ("".join(m))
    c.append(answer)
strg=""
for i in c:
    strg=strg+i
print(strg)




