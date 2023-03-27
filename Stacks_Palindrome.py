# Class Template for data in Stacks
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Main Palindrome
class Palindrome:
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

    # Check if the Word is Palindrome or Not
    def is_palindrome(self, string):
        # Convert the String to Uppercase and Remove Whitespaces
        string = string.upper().replace(" ", "")

        # Check if string is Empty or Contains Whitespace
        if string == "":
            print("Please Enter a Word!")
            return False

        # List of Characters from the String
        chars = list(string)

        # Push each Character into the Stack
        for char in chars:
            self.push(char)

        # Compare each Character and Popped off Characters from Stack
        for char in chars:
            if self.peek() != char:
                print("The word is not a palindrome.")
                return False
            self.pop()

        # If the Characters Match then the String is Palindrome
        print("The word is a palindrome.")
        return True


# Invoke Class Palindrome
p = Palindrome()

# Prompt the User to Enter a Word
w = input('Enter a word: ')

# Check if the Entered Word is Palindrome
p.is_palindrome(w)
