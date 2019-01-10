from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        return self.queue.add_at(0, value)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.stack.element_at(self.stack.length -1)
