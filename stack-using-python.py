# Build a stack using built in python array methods
class Stack:
    def __init__(self):
        # TODO: Initialize the Stack
        self.num_elements = 0
        self.items = []
        
    
    def size(self):
        # TODO: Check the size of the Stack
        return self.num_elements
    
    def push(self, item):
        # TODO: Push item onto Stack
        self.items.append(item)
        self.num_elements += 1

    def pop(self):
        # TODO: Pop item off of the Stack
        if self.size() == 0:
            return None
        else:
            self.num_elements -= 1
            return self.items.pop()
        


MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")