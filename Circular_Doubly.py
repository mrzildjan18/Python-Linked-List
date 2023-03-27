# Class Linked List Template
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Class Circular Doubly
class Circular_Doubly:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at beginning of the list
    def insert_beginning(self, data):
        node = Node(data)

        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            self.head = self.tail = node

    # Insert at the end of the list
    def insert_end(self, data):
        node = Node(data)

        if self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.head.prev = self.tail
            self.tail.next = self.head

        else:
            self.head = self.tail = node

    # Delete at the beginning of the List
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail

        else:
            print('The list is empty')

    # Delete at the end of the List
    def delete_end(self):
        if self.head:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    # Display output
    def display(self):
        if self.head:
            current = self.head

            while current.next != self.head:
                print(current.data, end=' ')
                current = current.next

            print(current.data, end=' ')

        else:
            print('The list is empty')

        # Check Head and Tail
        print()
        print('Head = ', self.head.data)
        print('Tail = ', self.tail.data)
        print('Head Prev = ', self.head.prev.data)
        print('Tail Next = ', self.tail.next.data)

    # Display output in reverse
    def display_reverse(self):
        if self.head:
            current = self.tail

            while current != self.head:
                print(current.data, end=' ')
                current = current.prev

            print(current.data, end=' ')

        else:
            print('The list is empty')

        # Check Head and Tail
        print()
        print('Head = ', self.head.data)
        print('Tail = ', self.tail.data)
        print('Head Prev = ', self.head.prev.data)
        print('Tail Next = ', self.tail.next.data)

    # Display all list in Even Numbers
    def display_even(self):
        if self.head:
            current = self.head

            while current.next != self.head:
                if current.data % 2 == 0:
                    print(current.data, end=' ')

                current = current.next

            if current.data % 2 == 0:
                print(current.data, end=' ')

        else:
            print('The list is empty')

    # Display all list in Odd Numbers
    def display_odd(self):
        if self.head:
            current = self.head

            while current.next != self.head:
                if current.data % 2 != 0:
                    print(current.data, end=' ')

                current = current.next

            if current.data % 2 != 0:
                print(current.data, end=' ')

        else:
            print('The list is empty')

# Create Object and Assign Values to Object
cd = Circular_Doubly()
print()
cd.insert_beginning(10)
cd.insert_beginning(8)
cd.insert_beginning(7)
cd.insert_beginning(5)
cd.insert_beginning(2)
print('Insert Beginning without Reverse')
cd.display()
print()

print('Insert Beginning with Reverse')
cd.display_reverse()
print()

# print('Insert End without Reverse')
# cd.display()
# print()
#
# print('Insert End with Reverse')
# cd.display_reverse()
# print()
#
# print('Delete Beginning without Reverse')
# cd.delete_beginning()
# cd.display()
# print()
#
# print('Delete Beginning with Reverse')
# cd.delete_beginning()
# cd.display_reverse()
# print()
#
# print('Delete End without Reverse')
# cd.delete_end()
# cd.display()
# print()
#
# print('Delete End with Reverse')
# cd.delete_end()
# cd.display_reverse()
# print()

print('Even Numbers Linked List')
cd.display_even()
print()
print()
print('Odd Numbers Linked List')
cd.display_odd()
print()
