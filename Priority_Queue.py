class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class QueuePriority:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data, priority):
        node = Node(data, priority)

        if not self.is_empty():
            if priority < self.front.priority:
                node.next = self.front
                self.front = node

            else:
                current = self.front
                while current.next:
                    if priority <= current.next.priority:
                        node.next = current.next
                        current.next = node
                        return
                    current = current.next

                self.rear.next = node
                self.rear = node
        else:
            self.front = self.rear = node

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')

        else:
            self.front = self.front.next

    def is_empty(self):
        return True if self.front is None else False

    def get_elements(self):
        current = self.front

        if self.is_empty():
            print('Queue is Empty')

        while current:
            print(current.data)
            current = current.next


queue = QueuePriority()
queue.enqueue('Zild', 4)
queue.enqueue('John', 2)
queue.enqueue('Kian', 1)
queue.enqueue('Paul', 4)
queue.dequeue()
queue.get_elements()
