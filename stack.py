from linkedlist import LinkedList
import copy

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def add(self, value):
        return self.stack.add(value)

    def get(self):
        element = self.stack[-1]
        del self.stack[-1]
        return element

    def peek(self):
        return self.stack[-1]

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return '{}'.format(self.stack.as_array())
