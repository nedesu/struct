import copy

class LinkedList:
    head = None

    length = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


    def add(self, value):
        node = self.Node(value)

        if self.empty():
            self.head = node
            self.length += 1
            return True

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = node
        self.length += 1
        return True


    def add_at(self, index, value):
        if index > self.length:
            return False

        node = self.Node(value)

        if index == 0:
            self.head, self.head.next = node, self.head
            self.length += 1
            return True

        current_node = self.head

        for i in range(index-1):
            current_node = current_node.next

        node.next, current_node.next = current_node.next, node

        self.length += 1
        return True


    def remove(self, index):
        if index >= self.length:
            return False

        node = self.head

        if index == 0:
            self.head = node.next
            self.length -= 1
            return True

        for i in range(index-1):
            node = node.next

        node.next = node.next.next
        self.length -= 1

        return True


    def rewrite(self, index, value):
        if index >= self.length:
            return False

        node = self.head

        for i in range(index):
            node = node.next

        node.value = value
        return True


    def pop(self):
        element = self.element(self.length - 1)
        self.remove(self.length - 1)
        return element


    def search_first(self, value):
        if self.empty():
            return False

        node = self.head
        index = 0

        if node.value == value:
            return 0

        while node.next:
            index += 1
            node = node.next
            if node.value == value:
                return index

        return False


    def search_first_in_array(self, index, value):
        if self.empty():
            return False

        node = self.head
        i = 0

        if node.value[index] == value:
            return 0

        while node.next:
            i += 1
            node = node.next
            if node.value[index] == value:
                return i

        return False


    def search_all(self, value):
        if self.empty():
            return False

        node = self.head
        list = []
        index = 0
        has_element = False

        if node.value == value:
            list.append(index)
            has_element = True

        while node.next:
            index += 1
            node = node.next
            if node.value == value:
                list.append(index)
                has_element = True

        if not has_element:
            return False

        return list


    def search_all_in_array(self, index, value):
        if self.empty():
            return False

        node = self.head
        list = []
        i = 0
        has_element = False

        if node.value[index] == value:
            list.append(0)
            has_element == True

        while node.next:
            i += 1
            node = node.next
            if node.value[index] == value:
                list.append(i)
                has_element = True

        if not has_element:
            return False

        return list


    def element(self, index):
        if index >= self.length:
            return False

        node = self.head

        for i in range(index):
            node = node.next

        return node.value


    def as_array(self):
        list = []

        if self.empty():
            return False

        node = self.head
        list.append(node.value)

        while node.next:
            node = node.next
            list.append(node.value)

        return list


    def copy(self):
        return copy.deepcopy(self)

    def empty(self):
        return self.length == 0
