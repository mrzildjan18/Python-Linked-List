# Class Template for data in Stacks
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Main Parenthesis
class Parenthesis:
    def __init__(self):
        self.top = None

    # Adds a New Element to the Top of the Stack
    def push(self, data):
        node = Node(data)

        if not self.is_empty():
            node.next = self.top

        self.top = node

    # Removes the Top Element from the Stack
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        else:
            self.top = self.top.next

    # Returns the Value of the Top Element in the Stack
    def peek(self):
        return self.top.data

    # Returns True if the Stack is Empty, and False otherwise
    def is_empty(self):
        return True if self.top is None else False

    # Check if the String is Parenthesis or Not
    def is_parenthesis(self, string):
        for char in string:
            if char == '(' or char == '[' or char == '{':
                # Push the opening parenthesis to the stack
                self.push(char)
            elif char == ')' or char == ']' or char == '}':
                # Check if the stack is empty or not
                if self.is_empty():
                    # If the stack is empty it means there is no matching parenthesis
                    return False

                # Value of the top element in the stack
                top = self.peek()

                # Check if the current closing parenthesis matches with the top element in the stack
                if (top == '(' and char == ')') or (top == '[' and char == ']') or (top == '{' and char == '}'):
                    # The current closing parenthesis matches to top element pop the top element
                    self.pop()
                else:
                    # The current closing parenthesis does not match to top element return False
                    return False

        # Check if the stack is empty or not
        if self.is_empty():
            return True
        else:
            return False

# Invoke Class Parenthesis
p = Parenthesis()

# Check if the string is a valid sequence of parenthesis or not
print(p.is_parenthesis(input('Enter Char: ')))
# print(p.is_parenthesis('[{(}]'))    # False
# print(p.is_parenthesis('[{()}]'))   # True
