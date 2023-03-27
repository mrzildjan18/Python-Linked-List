# Import random number generator
import random


# Node class representing a node in the queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Queue class representing the message queue
class Queue:
    def __init__(self):
        self.front = None  # front of the queue
        self.rear = None   # rear of the queue

    # method to add a message to the queue
    def enqueue(self, data):
        node = Node(data)

        if not self.is_empty():
            self.rear.next = node
            self.rear = node

        else:
            self.front = self.rear = node

    # method to remove a message from the front of the queue
    def dequeue(self):
        if self.is_empty():
            return None

        data = self.front.data
        self.front = self.front.next

        return data

    # method to check if the queue is empty
    def is_empty(self):
        return True if self.front is None else False


# Simulation parameters
arrival_rate = 30  # messages per minute
processing_rate = 40  # messages per minute

# Other variables
queue = Queue()
total_processed = 0
total_arrived = 0
total_sent = 0
total_requeue = 0
sent_attempts = [0] * 10

# Run simulation for 24 hours (1440 minutes)
for i in range(1440):

    # Check for new arrivals
    for j in range(arrival_rate):
        queue.enqueue(processing_rate)
        total_arrived += 1

    # Process queue messages
    for j in range(processing_rate):
        if not queue.is_empty():
            message = queue.dequeue()
            total_processed += 1

            # messages have a 75% chance of being sent on first attempt
            if random.random() <= 0.75:
                total_sent += 1
                sent_attempts[1] += 1

            # Messages have a 25% chance of being requeue
            else:
                total_requeue += 1
                sent_attempts[2] += 1
                queue.enqueue(message)


# Print message queue statistics
print("Total messages processed:", total_processed)
print("Average arrival rate:", round((total_arrived / 1440), 2))
print("Average number of messages sent per minute:", round((total_sent / 1440), 2))
print("Average number of messages in the queue in a minute:", round(((total_processed - total_sent) / 1440), 2))
print("Number of messages sent on the first attempt:", sent_attempts[1])
print("Number sent on the second attempt:", sent_attempts[2])
print("Average number of times messages had to be requeue:", round((sent_attempts[2] / total_processed), 2))
