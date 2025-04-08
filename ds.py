class LLNode:
    def __init__(self, node):
        self.node = node
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_items = 0

    def add_node(self, node, index):
        new_node = LLNode(node)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.num_items += 1

    def remove_node(self, index):
        if self.head is None:
            return None
        if index == 0:
            removed = self.head
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            removed = current.next
            current.next = removed.next
        self.num_items -= 1
        return removed.node

class Stack:
    def __init__(self):
        self.top = LinkedList()

    def push(self, node):
        self.top.add_node(node, 0)

    def pop(self):
        return self.top.remove_node(0)

    def peek(self):
        if self.top.head is None:
            return None
        return self.top.head.node
