class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stacks:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)

        if not self.is_empty():
            node.next = self.top

        self.top = node

    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            self.top = self.top.next

    def peek(self):
        return self.top.data

    def is_empty(self):
        return True if self.top is None else False

    def get_elements(self):
        current = self.top

        if self.is_empty():
            print('Stacks is Empty')

        while current:
            print(current.data)
            current = current.next


stack = Stacks()
word = input('Enter String: ')
for w in word:
    stack.push(w)

stack.get_elements()
print('Top Value: ', stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.get_elements()
print('Top Value: ', stack.peek())
