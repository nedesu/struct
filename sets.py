from linkedlist import LinkedList
import copy

class Sets:
    def __init__(self):
        self.set = LinkedList()

    def add(self, value):
        if not self.has(value):
            return self.set.add(value)
        return False

    def remove(self, value):
        if self.has(value):
            return self.set.remove(self.set.search_first(value))
        return False

    def union(self, *other_sets):
        new_set = self.copy()
        for set in other_sets:
            for value in set.values():
                new_set.add(value)
        return new_set

    def intersection(self, other_set):
        new_set = Sets()

        for value in self.values():
            if other_set.has(value):
                new_set.add(value)

        for value in other_set.values():
            if self.has(value):
                new_set.add(value)

        return new_set

    def difference(self, other_set):
        new_set = Sets()

        for value in self.values():
            if not other_set.has(value):
                new_set.add(value)

        for value in other_set.values():
            if not self.has(value):
                new_set.add(value)

        return new_set

    def subset(self, other_set):
        return other_set.values() == self.intersection(other_set).values()

    def has(self, value):
        return not self.set.search_first(value) is False

    def size(self):
        return self.set.length

    def values(self):
        return self.set.as_array()

    def __str__(self):
        return '{}'.format(self.set.as_array())

    def copy(self):
        return copy.deepcopy(self)
