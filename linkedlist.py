#append
#add_at
#remove_at
#pop

#search_first
#search_all

#element_at
#as_array

class LinkedList:
    head = None

    length = 0

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def append(self, value):
        node = self.Node(value)

        if not self.head:
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

    def remove_at(self, index):
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

    def pop(self):
        element = self.element_at(self.length - 1)
        self.remove_at(self.length - 1)
        return element

    def search_first(self, value):
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

    def search_all(self, value):
        node = self.head
        list = []

        if node.value == value:
            list.append(0)

        index = 0
        has_element = False

        while node.next:
            index += 1
            node = node.next
            if node.value == value:
                list.append(index)
                has_element = True

        if not has_element:
            return False

        return list




    def element_at(self, index):
        if index >= self.length:
            return False

        node = self.head

        for i in range(index):
            node = node.next

        return node.value

    def as_array(self):
        list = []

        if not self.head:
            return False

        node = self.head
        list.append(node.value)

        while node.next:
            node = node.next
            list.append(node.value)

        return list

    def is_empty(self):
        return self.length == 0
