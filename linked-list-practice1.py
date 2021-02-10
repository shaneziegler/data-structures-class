class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    new_node = Node(value)  
    new_node.next = self.head
    self.head = new_node

# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

def append(self, value):
    """ Append a value to the end of the list. """    
    # TODO: Write function to append here    
    if self.head is None:
        new_node = Node(value)
        self.head = new_node
        return
    current_node = self.head
    while current_node.next is not None:  
        current_node = current_node.next
    current_node.next = Node(value)

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head
    while node.value != value:
        if node.next is None:
            return None
        node = node.next
    return node

LinkedList.search = search

# Test search
print(linked_list.to_list())
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
print(linked_list.to_list())
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    
    node = self.head
    prev_node = node
    while node.value != value:
        if node.next is None:
            return None
        prev_node = node
        node = node.next
    if node == self.head:
        self.head = node.next
    else:
        prev_node.next = node.next
    node.next = None
    

LinkedList.remove = remove

# Test remove
print(linked_list.to_list())
linked_list.remove(1)
print(linked_list.to_list())
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
print(linked_list.to_list())
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
print(linked_list.to_list())
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    node = self.head
    if self.head.next is not None:
        self.head = self.head.next
    else:
        self.head = None
    return node.value

LinkedList.pop = pop

# Test pop
print(linked_list.to_list())
value = linked_list.pop()
print(linked_list.to_list())
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """
        
    # TODO: Write function to insert here    
    if self.head is None:
        self.append(value)
        return
    if pos == 0:
        self.prepend(value)
        return
    curr_pos = 0
    node = self.head
    while curr_pos < pos:
        curr_pos += 1
        prev_node = node
        node = node.next
        if node is None:
            self.append(value)
            return
    prev_node.next = Node(value)
    prev_node.next.next = node

LinkedList.insert = insert

# Test insert 
print(linked_list.to_list())
linked_list.insert(5, 0)
print(linked_list.to_list())
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
print(linked_list.to_list())
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
print(linked_list.to_list())
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    count = 0
    if self.head is None:
        return count
    node = self.head
    while node.next is not None:
        count += 1
    return count

LinkedList.size = size

# Test size function
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

