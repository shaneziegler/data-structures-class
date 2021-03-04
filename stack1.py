# Functionality
# Our goal will be to implement a Stack class that has the following behaviors:

# push - adds an item to the top of the stack
# pop - removes an item from the top of the stack (and returns the value of that item)
# size - returns the size of the stack
# top - returns the value of the item at the top of stack (without removing that item)
# is_empty - returns True if the stack is empty and False otherwise

class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        self.arr2 = [0 for _ in range(len(self.arr))]
        self.arr = self.arr + self.arr2


foo = Stack()
print(foo.arr)

# Define a class named Stack and add the __init__ method
# Initialize the arr attribute with an array containing 10 elements, like this: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Initialize the next_index attribute
# Initialize the num_elements attribute





foo.push("Test!")

foo = Stack()
foo.push("Test!")
print(foo.arr)
print("Pass" if foo.arr[0] == "Test!" else "Fail")

for x in range(10):
    foo.push(x)

print(foo.arr)