# Building a Queue in Python
# Before we start let us reiterate the key components of a queue.

# A queue is a data structure that consists of two main operations: enqueue and dequeue.

# Enqueue is when you add a element to the tail of the queue and a pop is when you remove an element from the head of the queue.

# Python 3.x conviently allows us to demonstate this functionality with a list. When you have a list such as [2,4,5,6] you can decide which end of the list is the front and the back of the queue respectively.

# Once you decide that, you can use the append, pop or insert function to simulate a queue.

# We will choose the first element to be the front of our queue and therefore be using the append and pop functions to simulate it. Give it a try by implementing the function below!

# Try Building a Queue

class Queue:
    def __init__(self):
        # TODO: Initialize the Queue
        self.q = []
    
    def size(self):
        # TODO: Check the size of the Queue
        return len(self.q)

    def enqueue(self, item):
        # TODO: Enter item into Queue
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")



