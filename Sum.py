"""

import sys

x = [1, 3, 5, 67, 45]
n = int(input("Enter the number of integers you would like to add in the list"))
for i in range(n):
    y = int(input("Enter the number to be appended to the list"))
    x.append(y)
x.sort()
m = int(input("Enter the number to be the sum"))
b=-1
for i in x:
    b = b + 1
    s=-1
    for j in x:
        s = s + 1
        if i == j:
            continue
        else:
            if i + j == m:
                print(i, j)
                print(b, s)
                print(x)
                sys.exit(0)
            else:
                continue
"""



import sys
nums = [6, 3, 5, 67, 45]
target =9
b=-1
for i in nums:
    b = b + 1
    s=-1
    for j in nums:
        s = s + 1
        if i == j:
            continue
        else:
            if i + j == target:
                print([b, s])
                sys.exit(0)
            else:
                continue