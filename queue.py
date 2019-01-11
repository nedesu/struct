from linkedlist import LinkedList
import copy

class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, value):
        return self.queue.add_at(0, value)

    def dequeue(self):
        return self.queue.pop()

    def enqueue_first(self, value):
        return self.queue.append(value)

    def dequeue_last(self):
        element = self.queue.element_at(0)
        self.queue.remove_at(0)
        return element

    def peek(self):
        return self.queue.element_at(self.queue.length -1)

    def copy(self):
        return copy.deepcopy(self)

class PriorityQueue(Queue):
    def enqueue(self, value, priority):
        if self.queue.is_empty():
            return self.queue.append((value, priority))

        queue = self.queue.as_array()

        for i in range(len(queue)):
            if queue[i][1] >= priority:
                return self.queue.add_at(i, (value, priority))

        return self.queue.append((value, priority))


    def enqueue_first(self, value, priority):
        if self.queue.is_empty():
            return self.queue.append((value, priority))

        queue = self.queue.as_array()

        for i in range(len(queue)):
            index = len(queue) - i - 1
            if queue[index][1] <= priority:
                return self.queue.add_at(index + 1, (value, priority))

        return self.queue.add_at(0, (value, priority))
