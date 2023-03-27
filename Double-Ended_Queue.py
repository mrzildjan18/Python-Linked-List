class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DoubleEndedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue_rear(self, data):
        node = Node(data)

        if not self.is_empty():
            self.rear.next = node
            self.rear = node

        else:
            self.front = self.rear = node

    def enqueue_front(self, data):
        node = Node(data)

        if not self.is_empty():
            node.next = self.front
            self.front = node

        else:
            self.front = self.rear = node

    def dequeue_rear(self):
        if self.is_empty():
            print('Queue is Empty')

        else:
            current = self.front

            while current.next:
                pre_current = current
                current = current.next

            pre_current.next = None
            self.rear = pre_current

    def dequeue_front(self):
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

        print('Front = ', self.front.data)
        print('Rear = ', self.rear.data)

    def get_elements_reverse(self):
        if self.is_empty():
            return

        current = self.rear

        while current != self.front:
            print(current.data)
            head = self.front
            while head.next != current:
                head = head.next
            current = head
        print(current.data)

        print('\nFront = ', self.front.data)
        print('Rear = ', self.rear.data)

    def divisible(self):
        if self.is_empty():
            return

        print('\nDivisible by 3: ')
        current = self.front
        while current:
            if current.data % 3 == 0:
                print(current.data)
            current = current.next


# Invoke Class and Method and Assign Values to Parameters
q = DoubleEndedQueue()
# Enqueue this data to the front of the Queue (2,4,5,6,10,12,12,45)
q.enqueue_front(2)
q.enqueue_front(4)
q.enqueue_front(5)
q.enqueue_front(6)
q.enqueue_front(10)
q.enqueue_front(12)
q.enqueue_front(12)
q.enqueue_front(45)
# Enqueue this data to the rear of the Queue (20,19,18,17,16,15)
q.enqueue_rear(20)
q.enqueue_rear(19)
q.enqueue_rear(18)
q.enqueue_rear(17)
q.enqueue_rear(16)
q.enqueue_rear(15)
# Dequeue in the Front Twice
q.dequeue_front()
q.dequeue_front()
# Dequeue in the Rear Twice
q.dequeue_rear()
q.dequeue_rear()
# Display the Queue in reverse Order
q.get_elements_reverse()
# Display a Queue of Divisible by 3
q.divisible()
