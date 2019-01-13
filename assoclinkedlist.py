from linkedlist import LinkedList

class AssocLinkedList(LinkedList):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def add(self, key, value):
        node = self.Node(key, value)

        if self.is_empty():
            self.head = node
            self.length += 1
            return True

        if self.element(key):
            return False

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = node
        self.length += 1
        return True


    def add_at(self, index, value):
        return False


    def remove(self, key):
        if self.is_empty() or not self.element(key):
            return False

        node = self.head

        if node.key is key:
            self.head = self.head.next
            self.length -= 1
            return True

        while node.next:
            if node.next.key is key:
                node.next = node.next.next
                self.length -= 1
                return True
            node = node.next

        return False


    def rewrite(self, key, value):
        if self.is_empty():
            return False

        node = self.head

        while node.next:
            if node.key is key:
                node.value = value
                return True
            node = node.next

        return False


    def element(self, key):
        node = self.head

        if node.key is key:
            return node.value

        while node.next:
            node = node.next
            if node.key is key:
                return node.value

        return False


    def element_at(self, index):
        return LinkedList.element(self, index)


    def search_first(self, value):
        if self.is_empty():
            return False

        node = self.head
        if node.value == value:
            return node.key

        while node.next:
            node = node.next
            if node.value == value:
                return node.key
        return False


    def search_first_in_array(self, index, value):
        if self.is_empty():
            return False

        node = self.head
        if node.value[index] == value:
            return node.key

        while node.next:
            node = node.next
            if node.value[index] == value:
                return node.key
        return False


    def search_all(self, value):
        if self.is_empty():
            return False

        node = self.head
        list = []
        has_element = False
        if node.value == value:
            list.append(node.key)
            has_element = True

        while node.next:
            node = node.next
            if node.value == value:
                list.append(node.key)
                has_element = True

        if has_element:
            return list

        return False


    def search_all_in_array(self, index, value):
        if self.is_empty():
            return False

        node = self.head
        list = []
        has_element = False
        if node.value[index] == value:
            list.append(node.key)
            has_element = True

        while node.next:
            node = node.next
            if node.value[index] == value:
                list.append(node.key)
                has_element = True

        if has_element:
            return list

        return False


    def get_index(self, key):
        if self.is_empty():
            return False

        node = self.head
        index = 1

        if node.key is key:
            return 0

        while node.next:
            node = node.next
            if node.key is key:
                return index
            index += 1
        return False
