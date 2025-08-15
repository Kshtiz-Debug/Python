# Create nodes
node1 = Node('1')
node2 = Node('B')
node3 = Node('C')

# Link nodes
node1.set_next_node(node2)
node2.set_next_node(node3)

# Traverse nodes
current_node = node1
while current_node:
    print(current_node.get_value())
    current_node = current_node.get_next_node()
