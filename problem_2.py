def get_min_max(arr):
    '''
    Function Purpose: This returns the minimum value and the maximum value
        of a python list of integers.
    Args:
       1. arr - a list of integers.
       
    Returns:
        The minimum and maximum values in tuptle form: (minimum, maximum).
    '''
    # This raises an error if the argument is not a python list.
    assert type(arr) == list, f'''
    The argument must be a python list.'''
    
    min_value = None
    max_value = None
    
    # If there is nothing in the array, this returns the tuple:
    # (None, None)
    if len(arr) < 1:
        return (min_value, max_value)
    
    # If there is something in the array, this runs a for loop that finds
    # the minimum and maximum values.
    else:
        for i in arr:
            if (min_value == None) and (max_value == None):
                min_value = i
                max_value = i
                continue
            if i > max_value:
                max_value = i
                continue
            if i < min_value:
                min_value = i
    return (min_value, max_value)

# This is the boilerplate example provided by Udacity.
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

# The below code should pass. The get_min_max funciton should produce
# (0,9)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# This is a case in which there is only one element in the python list.
one_element = [1]
print(get_min_max(one_element)) # This should produce (1,1).

# This edge case should produce (None, None), because the python list is
# empty.
len_0_list = []
print(get_min_max(len_0_list)) # This should produce (None, None).

# This is an edge case of big numbers ranging from 1000000000000 to
# 1000000000010. 
big_numbers = [i for i in range (1000000000000, 1000000000010, 1)]
random.shuffle(big_numbers)

# The below code should produce a minimum and maximum tuple of
# (1000000000000, 1000000000009).
print(get_min_max(big_numbers))