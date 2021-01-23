# Big O space efficiency/complexity

# 4*4 = 16 bytes
# int = 4 bytes
def our_constant_function():

    x = 3 # Type int
    y = 345 # Type int
    z = 11 # Type int

    answer = x+y+z

    return answer

# 4*n + 8
def our_linear_function(n):

    n = n # Type int
    counter = 0 # Type int
    list_ = [] # Assume that the list is empty (i.e., ignore the fact that there is actually meta data stored with Python lists)

    while counter < n:
        list_.append(counter)
        counter = counter + 1

    return list_

# Python refresher
# ^ bitwise XOR operator
# // integer division - whole numbers and rounds down
# 7 // 2 = 3
# -7 // 2 = -4

#multiple variable assignment in one command
# x, y, z = 2, 3, 4
# use all lowercase and underscores for var naming in python,
# dont use camelcase
x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
# * with a string makes multiple copies
# "cat"*3 makes "catcatcat"

print("Mohammed has {} balloons".format(27))
#Mohammed has 27 balloons
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))
print("mark like to eat {} kibbel while {} likes wet food".format(435,"ben"))

new_str = "The cow jumped over the moon."
new_str.split()
#['The', 'cow', 'jumped', 'over', 'the', 'moon.']

#slice [startpos:endpos+1]
#"Cat"[1:2] = "a"
#string is ordered but immutable
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]
# replace two items in list at once
sentence2[0:2] = ["We", "want"]

#Lists
# Useful Functions for Lists I
# len() returns how many elements are in a list.
# max() returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
# min() returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
# sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged.
# join method
# Join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
name = "-".join(["García", "O'Kelly"])
print(name)
# append method
# A helpful method called append adds an element to the end of a list.
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)
#tuples
x = (1, 2, 3)
x = 1, 2, 3
#immutable
#ordered
# can omit parathesis
tuple_test = 1, 2, 3
# Tuple unpacking
x, y, z = tuple_test
#Sets
#Sets are unordered, unique, and muttable
# Sets use {}
some_list = [1, 2, 1, 3]
some_set = set(some_list)
print(some_set)
# {1, 2, 3}
some_set.add(4)
print(some_set)
print(some_set.pop())
#returns random element in the set
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breath' in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())
print(sorted_keys)

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(max(sorted_keys))