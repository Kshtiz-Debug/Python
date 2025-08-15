x=6742
print(x)
if x<0:
    x=(-x)
    y = str(x)
    print("-"+y[::-1])
else:
    y = str(x)
    print(y[::-1])