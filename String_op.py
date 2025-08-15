x="ctfv*fv$uvj"
for i in range(len(x)):
    if (x[i]=='$' or x[i]=='&'):
        continue
    if (x[i-1]=='*'):
        if(x[i]=='*'):
            if(x[i+1]=='*'):
                continue
    print(x[i])
