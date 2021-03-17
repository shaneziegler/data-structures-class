# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        # Code here
        self.qstack = Stack()

        
    def size(self):
         # Code here
         return self.qstack.size()
        
    def enqueue(self,item):
        # Code here
        self.qstack.push(item)

        
    def dequeue(self):
        # Code here
        tempstack = Stack()
        while self.qstack.size() > 0:
            tempstack.push(self.qstack.pop())
        value = tempstack.pop()
        while tempstack.size() > 0:
            self.qstack.push(tempstack.pop())       
        return value






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