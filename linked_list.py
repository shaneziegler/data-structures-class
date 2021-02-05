# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(2)b
# head.next = Node(1)

# print(head.value)
# print(head.next.value)


class Question:
 def __init__(self,prompt,question):
    self.prompt = prompt
    self.question = question
questions_prompt = [
 "What is the color of orange? \n (a) Red \n (b) Orange \n (c) Green\n \n",
  "What is the color of lansones? \n (a) Yellow \n (b) Green \n (c) Black\n \n",
  "What is the color of Strawberry? \n (a) Blue \n (b) Pink \n (c) Yellow \n \n"
]
questions = [
 Question(questions_prompt[0], "b"),
 Question(questions_prompt[1], "a"),
 Question(questions_prompt[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.question:
            score += 1

    print(" You got" + " " + str(score) + "/" + str(len(questions)) + " " +"correct answer" )

run_test(questions)