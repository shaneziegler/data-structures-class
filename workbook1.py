# Workbook for class examples/tutorials
# Python refresher

# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    # TODO: Fill out the function here.
    result = []
    for semester in courses:
        for classid in courses[semester]:
            if classid == course:
                result.append(semester)
    
    # TODO: Return list of semesters here.
    return result



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []

# ################################################ #

# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))

# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)

# Now go back to generating more even numbers.
for i in range(100):
    print(next(my_gen))


def prod(a,b):
    # TODO change output to the product of a and b
    output = a * b
    return output
    
def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))


# ################################################ #
# Sudoku puzzle checker
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
correct3 = [[1,2,3],
           [3,1,2],
           [2,3,1]]

# Define a function check_sudoku() here:
def check_sudoku(puzzle):
    # Check each row to make sure number only appears once
    puzzle_size = len(puzzle)
    for row in puzzle:
        for i in range(puzzle_size):
            if row.count(i+1) != 1:
                return False
    #Transpose sudoku grid columns to rows        
    puzzle2 = []
    for y in range(puzzle_size):
        newrow = []
        for x in range(puzzle_size):
            newrow.append(puzzle[x][y])
        puzzle2.append(newrow)
    # Check each row(previously columns) to make sure number only appears once
    for row in puzzle2:
        for i in range(puzzle_size):
            if row.count(i+1) != 1:
                return False
    return True


    
    
print(check_sudoku(incorrect))
#>>> False
print(check_sudoku(correct))
#>>> True
print(check_sudoku(correct3))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False
# ################################################ #
# Udacity sudoko checker solution
# different implementation than mine

# An example solution for the check_sudoku() function

def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True

# ################################################### #
# Python Class Practice
class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month
        
    def birthday(self):
        self.age += 1

def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects

def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages 
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age =+ 1
            april_birthdays[person.name] = person.age
    # TODO: Modify the return statement 
    return april_birthdays

def get_most_common_month(people):
    # TODO:
    # Use the "months" dictionary to record counts of birthday months
    # for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 
              'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
              'November':0, 'December':0}
    for person in people:
        bdmonth = person.birthday_month
        months[bdmonth] += 1

    most_bd_month = ''
    max_bd_count = 0
    for month in months:
        if months[month] > max_bd_count:
            max_bd_count = months[month]
            most_bd_month = month

    # TODO: Modify the return statement.
    return most_bd_month


def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
    ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
    months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))



test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August
# ################################################### #
