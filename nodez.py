a=(12,None)
b=(13,a)
print(type(a))
print(type(b))
print(b)










# (value, next_node)
node3 = (123,None)
node2 = (10, node3)
node1 = (5, node2)


print(node1)
# Traverse
current = node1

print(current)
while current:
    print(current[0])       # value
    current = current[1]    # next
