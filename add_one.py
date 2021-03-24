def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    if arr[-1] < 9:
        arr[-1] += 1
    else:
        x = arr[-1]
    return arr


# A helper function for Test Cases
def test_function(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    carry_one = False
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 9:
            carry_one = True
            arr[i] = 0
        else:
            arr[i] += 1
            carry_one = False
            break
            
    if carry_one:
        arr = '1' + arr
    return arr

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)