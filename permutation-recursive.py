# Permutation recursive

# import copy                                           # `copy` module

# list1 = [0, 1, 2]
# list2 = [7, 8, 9]                                     
# compoundList1 = [list1, list2]                        # create a compound object


# '''ASSIGNMENT OPERATION - Points a new reference to the existing object.'''
# compoundList2 = compoundList1

# # id() - returns the identity of the object passed
# print(id(compoundList1) == id(compoundList2))          # True - compoundList2 is the same object as compoundList1
# print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


# '''SHALLOW COPY'''
# compoundList2 = copy.copy(compoundList1)

# print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
# print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


# '''DEEP COPY'''
# compoundList2 = copy.deepcopy(compoundList1)

# print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
# print(id(compoundList1[0]) == id(compoundList2[0]))    # False - compoundList2[0] is now a new object

# Code

import copy


def permute_org(inputList):
    if len(inputList) == 0:
        return [[]]
    elif len(inputList) == 1:
        return [copy.deepcopy(inputList)]
    else:
        result =[]
        for i in range(len(inputList)):
            x = inputList.pop(0)
            perms = permute(inputList)
                # result = perm[:i] + list(x)
                # result = perm[:i].append(x)
                # result = result + perm[i+1:]
            for perm in perms:
                # result = copy.deepcopy(plist)
                perm.append(x)
            # result.extend(perms)
            result = result + perms
            inputList.append(x)
        return result


def permute_me(inputList):
    if len(inputList) == 1 or len(inputList) == 0:
        # return [copy.deepcopy(inputList)] works
        # a = inputList
        # b = [inputList]
        # c = copy.deepcopy(inputList)
        # d = [copy.deepcopy(inputList)]
        # e = inputList[:]
        f = [inputList[:]] # works

        # print(hex(id(inputList)))
        # print(hex(id(a)))
        # print(hex(id(b)))
        # print(hex(id(b[0])))
        # print(hex(id(c)))
        # print(hex(id(d)))
        # print(hex(id(e)))
        # print(hex(id(f)))

        return f
    else:
        result =[]
        for _ in range(len(inputList)):
            x = inputList.pop(-1)
            perms = permute(inputList)
            for perm in perms:
                perm.insert(0,x)
            result += perms
            inputList.insert(0,x)
        return result



# Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

# Recursive Solution 
"""
Args: myList: list of items to be permuted
Returns: compound list: list of permutation with each permuted item being represented by a list
"""
import copy                                # We will use `deepcopy()` function from the `copy` module

def permute_udacity_org(inputList):
    
    # a compound list
    finalCompoundList = []                  # compoundList to be returned 
    
    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])
    else:
        finalCompoundList = []    
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        # Recursive function call
        sub_compoundList = permute(rest_list)
        
        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:
            
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList

def permute(inputList):
    
    # a compound list
    # finalCompoundList = []                  # compoundList to be returned 
    
    # Terminaiton / Base condition
    if len(inputList) == 0:
        # finalCompoundList.append([])
        return [[]]
    else:
        finalCompoundList = []    
        first_element = inputList[0]        # Pick one element to be permuted
        sub_compoundList = permute(inputList[1:])
        
        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:
            
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = aList[:]
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList += [bList]
                
    return finalCompoundList

r = permute([])
r = permute([1])
r = permute([1,2,3])
r = permute_me([1,2,3])
# r = permute([1,2,3,4, 5])

print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")

