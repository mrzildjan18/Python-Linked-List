# Class Linked List Template
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Header Circular
class Header_Grounded:
    def __init__(self):
        self.head = Node(None)

    # Method insert at the beginning of the list
    def insert_beginning(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head.next
            self.head.next = node
        else:
            self.head.next = node

    # Method insert at the end of the list
    def insert_end(self, data):
        node = Node(data)
        if self.head:
            current = self.head

            while current.next:
                current = current.next

            current.next = node
        else:
            self.head.next = node

    # Method delete at the beginning of the list
    def delete_beginning(self):
        if self.head:
            self.head.next = self.head.next.next

        else:
            print('The list is empty')

    # Method delete at the end of the list
    def delete_end(self):
        if self.head:
            current = self.head

            while current.next:
                pre_current = current
                current = current.next

            pre_current.next = current.next

        else:
            print('The list is empty')

    # Method display all nodes
    def display(self):
        if self.head:
            current = self.head

            while current:
                print(current.data, end=' ')
                current = current.next
        else:
            print('The list is empty')

# Object Creation and Assign Values to Objects
hd = Header_Grounded()
hd.insert_beginning(10)
hd.insert_beginning(8)
hd.insert_beginning(7)
print('Insert beginning at the list')
hd.display()
print()

print()
hd.insert_end(11)
hd.insert_end(8)
hd.insert_end(6)
print('Insert at the end of the list')
hd.display()
print()

print()
print('Delete at the beginning of the list')
hd.delete_beginning()
hd.display()
print()

print()
print('Delete at the end of the list')
hd.delete_end()
hd.display()
print()
