from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.element_at(self.stack.length -1)
