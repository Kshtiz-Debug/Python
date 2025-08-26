def mini(L):
    x=L[0]
    for i in L:
        if i<x:
            x=i
    return x
A=[1,2,35,756,25363,245632353,5,5632,0,7542,541631,-541,-245,32,32314,54,42,3,31,1,2,23,53423]
print(mini(A))
print(sorted(A))


def sort(L):
    x=mini(L)
    L.remove(x)
    n=len(L)
    if n==1:
        return [x]
    return [x]+sort(L)

print(sort(A))
