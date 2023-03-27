class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self,data): #
        node = Node(data)

        if self.head:
            node.next = self.head
            self.head = node
            self.head = node
            self.tail.next = self.head
        else:
            self.head = node
            self.tail = node

    def insert_end(self, data):
        node = Node(data)

        if self.head:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
        else:
            self.head = self.tail = node
            self.head.next = self.head

    def insert_before(self, data, pos):
        search_val = self.pos = pos
        new_node = Node(data)

        if self.head:
            current = self.head
            prev = current

            while current.data != pos:
                prev = current
                current = current.next

            if prev == self.head:
                self.tail.next = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                prev.next = new_node
                new_node.next = current

        else:
            self.head = self.tail = new_node
            self.head.next = self.head

    def insert_after(self, data, pos):
        search_val = self.pos = pos
        new_node = Node(data)

        if self.head:

            current = self.head
            post_curr = current.next

            while current.data != search_val:
                current = current.next
                post_curr = current.next

            if current == self.tail:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                current.next = new_node
                new_node.next = post_curr
        else:
            self.head = self.tail = new_node
            self.head.next = self.head

    def delete_beginnging(self):
        if self.head:
            self.head = self.head.next
            self.tail.next = self.head
        else:
            print("linked List is Null")

    def del_end(self):
        if self.head:
            current = self.head
            while current.next != self.head:
                pre_current = current
                current = current.next
            self.tail = pre_current
            self.tail.next = self.head
        else:
            print("linked List is Null")

    def display(self):
        if self.head:
            current = self.head

            while current.next != self.head:
                print(current.data, ' ', end='')
                current = current.next
            print(current.data)
        else:
            print('linked List is Null')

c = Circular()
c.insert_end(10)
c.insert_end(5)
c.insert_end(4)
c.insert_end(9)
c.insert_end(3)
c.insert_end(8)
c.insert_end(100)
c.delete_beginnging()
c.insert_before(100000, 5)
c.insert_after(100000, 4)
c.display()
