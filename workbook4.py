# Truth Value Testing
# If we use a non-boolean object as a condition in an if statement in place of the boolean expression, Python will check for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of an object in Python is considered True unless specified as False in the documentation.

# Here are most of the built-in objects that are considered False in Python:

# constants defined to be false: None and False
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '"", (), [], {}, set(), range(0)


book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
# word count dictionary using dictonary get method
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
# intead using a for loop
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1    

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit in fruits:
    if fruit in basket_items:
        result += basket_items.get(fruit)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for item in basket_items:
    if item in fruits:
        fruit_count += basket_items.get(item)
    else:
        not_fruit_count += basket_items.get(item)
#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count


print(fruit_count, not_fruit_count)

# udacity solution
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.  There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))

#factorial while loop
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)

#For loop factorial
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for current in range(1,number+1):
    # multiply the product so far by the current number
    product *= current
    
# print the factorial of number
print(product)

#Nearest Square
#My solution
limit = 40

# write your while loop here
start_num = 1
while (start_num ** 2) < limit:
    nearest_square = start_num ** 2
    start_num += 1
    
print(nearest_square)
#Udacity Solution
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

#Exactly 140 char long newsticker
#Use break statement
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for prime in check_prime:
    for num in range(2, prime):
        if prime % num == 0:
            print(str(prime) + " is not a prime number")
            print(str(prime) + " is a factor of " + str(num))
            break
        if num == (prime - 1):
            print(str(prime) + " is a prime number")
            break

# Zip work
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    x = "{}: {}, {}, {}".format(*point)
    points.append(x)

for point in points:
    print(point)

## Use zip to make dictionary
# my solution
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]
cast = {}
for key, value in zip(cast_names, cast_heights):
    cast[key] = value

print(cast)

## udacity solution
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)


# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = zip(*cast)
print(names)
print(heights)

#enumerate
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
for i ,person in enumerate(cast):
    cast[i] += " " + str(heights[i])
print(cast)

