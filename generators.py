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
    i = 
    while i < len(iterable):
        yield start+i, iterable[i]
        i += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
print("\n\n\n")   


###
# Quiz: Chunker
# If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), being able to take and use chunks of it at a time can be very valuable.

# Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

def chunker(iterable, size):
    # Implement function here
    i = 0
    while i < len(iterable):
        yield iterable[i:i+size]
        i += size


for chunk in chunker(range(25), 4):
    print(list(chunk))

###
# Generator Expressions
# Generators with list comprehesions

# sq_list = [x**2 for x in range(10)]  # this produces a list of squares

# sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
