# Problem Statement
# Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers.
#  Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

# Example:

# linked list = 1 2 3 4 5 6
# output = 1 3 5 2 4 6

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """


    moved = True
    end = False

    if not head.next:
        end = True

    while moved:
        moved = False
        curr_node = head
        prev_node = None
        end = False
        while not end:
            lnode = curr_node
            lnode_value = lnode.data
            rnode = curr_node.next
            rnode_value = rnode.data
            if (lnode.data % 2 == 0) and (rnode.data % 2 == 1): # If even number on left and odd on right
                lnode.next = rnode.next
                rnode.next = lnode
                moved = True
                if not prev_node:
                    head = rnode
                else:
                    prev_node.next = rnode
                prev_node = rnode
                curr_node = lnode
            else:
                prev_node = curr_node
                curr_node = curr_node.next
            if not curr_node.next:
                end = True 
    
    return head
            

    

# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]
    
    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)    
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")            
    except Exception as e:
        print("Fail")

arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)    