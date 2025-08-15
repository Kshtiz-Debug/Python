"""m=0
s="(()"
for i in range(len(s)):
    if s[i]=="(":
        if i==len(s)-1:
            print(m)
        if s[i+1]==")":
            m=m+2
print(m)
"""






"""............................................................................................./"""


"""
s="()(())"
x=[]
for i in s:
    x.append(i)
print(x)
flag=True
m=0
c=0
while(flag):
    c=c+1
    for i in range(len(x)):
        if x[i]=='(':
            if i!=len(x)-1:
                if x[i + 1] == ")":
                    m=m+2
                    x.remove(x[i])
                    x.remove(x[i+1])
    if c==3:
        flag=False
print(m)


"""









s = "()(())())))("
stack = []
m = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)  # Store index of '('
    elif stack:
        stack.pop()
        m=m+2
print(m)
