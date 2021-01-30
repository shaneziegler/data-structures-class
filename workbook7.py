how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)


# We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a string as a line of Python.

result = eval(input("Enter an expression: "))
print(result)