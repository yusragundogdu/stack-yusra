from ds import Stack
from import_nodes import import_csv

print("CSV'den node'lar okunuyor...")  

stack = Stack()
nodes = import_csv("coordinates.csv")

print(f"{len(nodes)} tane node bulundu.")  

for i in range(len(nodes)):
    stack.push(nodes[i])

for i in range(len(nodes)):
    node = stack.pop()
    print("Removed Node")
    print("ID: {}, Name: {}".format(node.id, node.name))