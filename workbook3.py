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
