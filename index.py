from assoclinkedlist import AssocLinkedList

ll = AssocLinkedList()
ll.add(321, 'boi')
ll.add('1', 521)
ll.add('haha', 'boi')
ll.add(2, 'jest')
ll.add(4, 'chetire')
ll.add('hell', 'boi')
print(ll.search_all('boi'))
print(ll.as_array())
print(ll.element(4))
