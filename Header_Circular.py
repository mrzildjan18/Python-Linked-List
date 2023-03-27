# Class Linked List Template
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Header Circular
class Header_Circular:
    def __init__(self):
        self.head = Node(None)
        self.tail = None

    # Method insert at the beginning of the list
    def insert_beginning(self, data):
        node = Node(data)
        if self.head.next:
            node.next = self.head.next
            self.head.next = node
        else:
            self.head.next = self.tail = node
            self.tail.next = self.head

    # Method insert at the end of the list
    def insert_end(self, data):
        node = Node(data)

        if self.head.next:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.head.next = self.tail = node
            self.tail.next = self.head

    # Method delete at the beginning of the list
    def delete_beginning(self):
        if self.head:
            self.head.next = self.head.next.next
            self.tail.next = self.head

        else:
            print('The list is empty')

    # Method delete at the end of the list
    def delete_end(self):
        if self.head:
            current = self.head

            while current.next != self.tail:
                current = current.next

            self.tail = current
            self.tail.next = self.head
        else:
            print('The list is empty')

    # Method display all nodes
    def display(self):
        if self.head:
            current = self.head

            while current:
                print(current.data, end=' ')
                if current.next == self.head:
                    break
                current = current.next

        else:
            print('The list is empty')

        # Check for Head and Tail
        print()
        print('Head = ', self.head.data)
        print('Tail = ', self.tail.data)

# Object Creation and Assign Values to Objects
hd = Header_Circular()
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
