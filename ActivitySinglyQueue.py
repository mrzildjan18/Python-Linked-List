# Class Queue Template
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Queue
class Queue:
    # Constructor
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert at the end of Queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    # Delete at the end of Queue
    def dequeue(self):
        if self.front:
            current = self.front

            while current.next:
                pre_current = current
                current = current.next

            pre_current.next = None
            self.rear = pre_current

            if current == self.front:
                self.front = None
                return
        else:
            print('Queue is Empty')

    # Display of all Queue
    def display(self):
        current = self.front

        if self.front:
            print('Head = ', self.front.data)
            print('Tail = ', self.rear.data)

        if current:
            while current:
                print(current.data, end=' ')
                current = current.next

        else:
            print('Queue is Empty')

    # Sum of all Queues
    def sum(self):
        if self.front:
            current = self.front

            sum = 0
            while current:
                sum = sum + current.data
                current = current.next
            print('\nSum of all Queue = ', sum)

# Assign Values to Objects and Initialize
q = Queue()
q.enqueue(8)
q.enqueue(6)
q.enqueue(4)
q.dequeue()
q.display()
q.sum()

