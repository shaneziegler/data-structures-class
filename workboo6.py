egg_count = 0

def buy_eggs():
    print(egg_count)

buy_eggs()

egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()

# In the last video, you saw that within a function, we can print a global variable's value successfully without an error. This worked because we were simply accessing the value of the variable. 
# If we try to change or reassign this global variable, however, as we do in this code, we get an error. Python doesn't allow functions to modify variables that aren't in the function's scope.

# Documentation
# Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. 
# Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

# Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose. 
# If you feel that this is sufficient documentation you can end the docstring at this point; single line docstrings are perfectly acceptable, as in the example above.



# Lambda functions
# def multiply(x, y):
#     return x * y

multiply = lambda x, y: x * y

multiply(4, 7)

# Components of a Lambda Function
# The lambda keyword is used to indicate that this is a lambda expression.
# Following lambda are one or more arguments for the anonymous function separated by commas, followed by a colon :. Similar to functions, the way the arguments are named in a lambda expression is arbitrary.
# Last is an expression that is evaluated and returned in this function. This is a lot like an expression you might see as a return statement in a function.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

averages = list(map(lambda num_list : sum(num_list)/len(num_list), numbers))
print(averages)

###

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston", "Minneapolis", "Seattle"]

def is_short(name):
    return len(name) < 10

# short_cities = list(filter(is_short, cities))


short_cities = list(filter(lambda city : len(city) < 10, cities))

print(short_cities)


