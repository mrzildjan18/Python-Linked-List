class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node

    def insert_end(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        else:
            self.head = node

    def insert_before(self, data, search_value):
        found = False
        if self.head:
            current = self.head

            while current:
                if current.data == search_value:
                    node = Node(data)
                    node.next = current
                    node.prev = current.prev
                    current.prev.next = node
                    current.prev = node
                    found = True
                    break

                current = current.next
            if not found:
                print('Search value not found')
        else:
            print('List is null')


    def insert_after(self, data, search_value):
        found = False
        if self.head:
            current = self.head

            while current:
                if current.data == search_value:
                    node = Node(data)
                    node.next = current.next
                    node.prev = current
                    current.next.prev = node
                    current.next = node
                    found = True
                    break

                current = current.next
            if not found:
                print("search value not found")
        else:
            print("List is null")


    def delete_beginning(self):
        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
            current = self.head

            while current.next:
                current = current.next
            current.prev.next = None

    def delete_given_node(self, search_value):
        found = False
        if self.head:
            current = self.head
            while current:
               if current.data == search_value:
                   current.prev.next = current.next
                   current.next.prev = current.prev
                   found = True
               current = current.next

            if not found:
                print("search value not found")
        else:
            print("list is empty")


    def display(self):
        if self.head:
            current = self.head

            while current:
                print(current.data, ' ', end='')
                current = current.next
        else:
            print("List is empty!")


    def display_reverse(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            while current:
                print(current.data, ' ', end='')
                current = current.prev
        else:
            print("Linked List is empty!")


d = Doubly()
d.insert_beginning(10)
d.insert_beginning(5)
d.insert_beginning(4)
d.insert_beginning(9)
d.insert_beginning(2)
d.delete_beginning()
d.insert_before(100000, 5)
d.insert_after(100000, 4)
d.delete_given_node(100000)
d.display()
