from linkedlist import LinkedList
import copy

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def add(self, value):
        return self.queue.add_at(0, value)

    def get(self):
        element = self[-1]
        del self[-1]
        return element

    def add_fistr(self, value):
        return self.queue.add(value)

    def get_last(self):
        element = self.queue[0]
        del self.queue[0]
        return element

    def peek(self):
        return self.queue[-1]

    def copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return '{}'.format(self.queue)

class PriorityQueue(Queue):
    def add(self, value, priority):
        if self.queue.is_empty():
            return self.queue.add((value, priority))

        queue = self.queue.as_array()

        for i in range(len(queue)):
            if queue[i][1] >= priority:
                return self.queue.add_at(i, (value, priority))

        return self.queue.add((value, priority))


    def add_first(self, value, priority):
        if self.queue.is_empty():
            return self.queue.add((value, priority))

        queue = self.queue.as_array()

        for i in range(len(queue)):
            index = len(queue) - i - 1
            if queue[index][1] <= priority:
                return self.queue.add_at(index + 1, (value, priority))

        return self.queue.add_at(0, (value, priority))
