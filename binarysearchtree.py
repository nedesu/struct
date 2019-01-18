import copy

class BinarySearchTree:
    root = None
    length = 0

    class Leaf:
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.rigth_child = None

    def add(self, value):
        leaf = self.Leaf(value)

        if self.empty():
            self.root = leaf
            self.length += 1
            return True

        parent = self.root
        while True:
            if parent.value == value:
                return False

            if parent.value > value:
                if parent.left_child:
                    parent = parent.left_child
                    continue
                else:
                    parent.left_child = leaf
                    self.length += 1
                    return True

            else:
                if parent.rigth_child:
                    parent = parent.rigth_child
                    continue
                else:
                    parent.rigth_child = leaf
                    self.length += 1
                    return True


    def branch(self, value):
        if self.empty():
            return False

        parent = self.root
        result = []

        while True:
            if parent.value == value:
                result.append({'value': parent.value, 'direction': None})
                return result

            if parent.value > value:
                if not parent.left_child:
                    return False
                result.append({'value': parent.value, 'direction': 'left'})
                parent = parent.left_child
                continue

            else:
                if not parent.rigth_child:
                    return False
                result.append({'value': parent.value, 'direction': 'rigth'})
                parent = parent.rigth_child
                continue


    def has(self, value):
        if self.empty():
            return False

        parent = self.root
        while True:
            if parent.value == value:
                return True

            if parent.value > value:
                if parent.left_child:
                    parent = parent.left_child
                else:
                    return False

            else:
                if parent.rigth_child:
                    parent = parent.rigth_child
                else:
                    return False


    def empty(self):
        return self.length == 0
