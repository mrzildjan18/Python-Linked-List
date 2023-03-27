class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        current = self.head

        if current:
            while current.next:
                current = current.next

            current.next = new_node
            new_node.next = None
        else:
            self.head = new_node

    def insert_before_node(self, data, search_value):
        new_node = Node(data)
        if self.head:
            current = self.head

            while current.data != search_value:
                pre_current = current
                current = current.next

            pre_current.next = new_node
            new_node.next = current
        else:
            print('HEAD is null')

    def insert_after_node(self, data, search_value):
        new_node = Node(data)

        if self.head:
            current = self.head

            while current.data != search_value:
                current = current.next
            post_current = current.next
            current.next = new_node
            new_node.next = post_current

        else:
            print('HEAD is null')

    def delete_end(self):
        if self.head:
            current = self.head
            while current.next:
                pre_current = current
                current = current.next

            pre_current.next = None

        else:
            print('HEAD is null')

    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Head is null")

    def display(self):
        current = self.head
        if current:

            while current:
                print(current.data, end=' ')
                current = current.next
        else:
            print("Head is null")


s = Singly()
s.insert_beginning(1)
s.insert_beginning(2)
s.insert_beginning(3)
s.insert_end(4)
s.insert_end(5)
s.insert_end(6)
s.insert_end(7)
s.insert_before_node(82, 1)
s.insert_after_node(11, 4)
s.insert_after_node(22, 11)
# s.delete_end()
# s.delete_beginning()
s.display()
