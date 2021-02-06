# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(2)b
# head.next = Node(1)

# print(head.value)
# print(head.next.value)


# class Question:
#  def __init__(self,prompt,question):
#     self.prompt = prompt
#     self.question = question
# questions_prompt = [
#  "What is the color of orange? \n (a) Red \n (b) Orange \n (c) Green\n \n",
#   "What is the color of lansones? \n (a) Yellow \n (b) Green \n (c) Black\n \n",
#   "What is the color of Strawberry? \n (a) Blue \n (b) Pink \n (c) Yellow \n \n"
# ]
# questions = [
#  Question(questions_prompt[0], "b"),
#  Question(questions_prompt[1], "a"),
#  Question(questions_prompt[2], "b"),
# ]
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.question:
#             score += 1

#     print(" You got" + " " + str(score) + "/" + str(len(questions)) + " " +"correct answer" )

# run_test(questions)

###

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    head = None
    for i,value in enumerate(input_list):
        if head is None:
            head = Node(value)
            current_node = head
        else:
            current_node.next = Node(value)
            current_node = current_node.next
    return head

### Test Code
def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: "  + e)
        
        

input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)
