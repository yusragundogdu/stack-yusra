# Implementation of stack using phyton lists
from nodes import *
from ds import *

try:
    stack_test = Stack()
    print("Stack sınıfı bulundu ve başarıyla oluşturuldu!")
except NameError as e:
    print(f"Hata: {e}")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")

# Stack initialization
stack = Stack()

nodes = import_csv("coordinates.csv")

# Add nodes to the stack using Linked Lists
for i in range(len(nodes)):
    stack.push(nodes[i])

# Pop the nodes from the stack using phyton lists
for i in range(len(nodes)):
    node = stack.pop()
    print("Removed Node")
    print("ID: {}, Name:  {}".format(node.id, node.name))    