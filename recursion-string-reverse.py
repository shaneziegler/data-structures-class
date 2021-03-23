# Reversing a String
# The goal in this notebook will be to get practice with a problem that is frequently solved by recursion: Reversing a string.

# Note that Python has a built-in function that you could use for this, but the goal here is to avoid that and understand how it can be done using recursion instead.

# Exercise - Write the function definition here

# Code

def reverse_string(input):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """
    
    # TODO: Write your recursive string reverser solution here
    
    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""
    
    first_char = input[0]
    the_rest = input[1:]
    new_str = reverse_string(the_rest)
    return new_str + first_char

# Test Cases
    

reverse_string("abc")

print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")

