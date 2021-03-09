# Reverse Polish Notation
# Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.

# When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands. For example: 5 + 7 - 3 * 8

# However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *

# The above expression would be evaluated as (3 + 1) * 4 = 16

# The goal of this exercise is to create a function that does the following:

# Given a postfix expression as input, evaluate and return the correct final answer.
# Note: In Python 3, the division operator / is used to perform float division. So for this problem, you should use int() after every division to convert the answer to an integer.

# 1. If a value appears next in the expression, push this value on to the stack.

# 2. If an operator appears next, pop two items from the top of the stack and push the result of the operation on to the stack.

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    # TODO: Iterate over elements 
    stack = Stack()
    for x in input_list:
        if x in ['+', '-', '/', '*']:
            val1 = stack.pop()
            val2 = stack.pop()
            if x == '+':
                val3 = val1 + val2
            if x == '-':
                val3 = val1 - val2
            if x == '*':
                val3 = val1 * val2
            if x == '/':
                val3 = val1 / val2
            stack.push(val3)
        else:
            stack.push(x)
    return stack.pop()
    
    

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)