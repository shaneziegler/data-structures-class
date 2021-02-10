# Helper Code

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

    
def reverse(linked_list):
    rev_list = LinkedList()
    
    node = linked_list.head
    new_node = Node(node.value)
    rev_list.head = new_node
    
    while node.next is not None:
        temp_node = new_node
        node = node.next
        new_node = Node(node.value)
        new_node.next = temp_node
        rev_list.head = new_node
    return rev_list

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")