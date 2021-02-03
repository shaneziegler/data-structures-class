def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    print(x)

print("\n\n\n")    
###
# Quiz: Implement my_enumerate
# Write your own generator function that works like the built-in function enumerate.

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    i = 0
    while i < len(iterable):
        yield start+i, iterable[i]
        i += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
