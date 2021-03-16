class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue_size = 0

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.queue_size = 1
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.queue_size += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.queue_size -= 1
        return value


    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty:
            return None
        else:
            return self.head.value

class Queue_array:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0


    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index

    def enqueue(self, value):
        # enqueue new element
        if self.queue_size == len(self.arr):
            self._handle_queue_capacity_full()

        self.arr[self.next_index] = value
        self.queue_size += 1
        print(self.next_index)
        print(self.next_index+1)
        print(len(self.arr))
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):
        # check if queue is empty
        if self.is_empty():
            self.front_index = -1   # resetting pointers
            self.next_index = 0
            return None

        # dequeue front element
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.front_index == -1 or self.queue_size == 0

    def front(self):
        if self.is_empty:
            return None
        else:
            return self.arr[self.front_index]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)