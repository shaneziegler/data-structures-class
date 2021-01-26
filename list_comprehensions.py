#
# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
print(first_names)

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)



# other stuff from chat

# word = "cat"
# index = len(word)
# while index <= len(word):
#     print(word[index-1])
#     index -= 1

# def until_dot(string, target):
#     index = 0
#     while index < len(string):
#         if string[index] != target:
#             print("Nope...")
#             index += 1
#         else:
#             print("There you are you little bugger!")
#             break

# until_dot("Hello." , ".")



# def until_dot2(string, target):
#     for char in string:
#         if char != target:
#             print("Nope...")
#         else:
#             print("There you are you little bugger!")
#             break

# until_dot2("Hello." , ".")

# def until_dot3(string, target):
#     if target in string:
#         print('There you are you little bugger!')
#     else:
#         print('Nope, not in string')