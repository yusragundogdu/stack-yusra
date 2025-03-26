class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self.top.data

    def get_size(self):
        return self.size

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")