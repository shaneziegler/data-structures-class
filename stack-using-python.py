class Stack:
    def __init__(self):
         # TODO: Initialize the Stack
        
    
    def size(self):
         # TODO: Check the size of the Stack
    
    def push(self, item):
         # TODO: Push item onto Stack

    def pop(self):
         # TODO: Pop item off of the Stack

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