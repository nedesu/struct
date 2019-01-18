from linkedlist import LinkedList
import copy

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, value):
        return self.stack.add(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.element(self.stack.length -1)

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return '{}'.format(self.stack.as_array())
