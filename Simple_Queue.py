class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if not self.is_empty():
            self.rear.next = node
            self.rear = node

        else:
            self.front = self.rear = node

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')

        else:
            self.front = self.front.next

    def peek(self):
        return self.front.data

    def is_empty(self):
        return True if self.front is None else False

    def get_elements(self):
        current = self.front

        if self.is_empty():
            print('Queue is Empty')

        while current:
            print(current.data)
            current = current.next


queue = SimpleQueue()
queue.enqueue(8)
queue.enqueue(6)
queue.enqueue(4)
queue.dequeue()
queue.get_elements()
