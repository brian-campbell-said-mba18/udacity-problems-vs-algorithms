def sort_012(py_list_012, debug_mode = False):
    '''
    Function Purpose: The purpose of this function is to sort a list of 0s,
        1s, and 2s in one traversal.
    
    Arguments: A list of 0s, 1s, and 2s, py_list_012, and debug_mode. If
        debug_mode is set to True, the print statements in this list
        are activated in order to detect bugs.
        
    Returns: The newly sorted list, py_list_012.

    Reference: Reference 1 from Refernces.
    '''
    
    # This code simply returns py_list_012 in the event that the 
    # length of py_list_012 is 0 or 1.
    if len(py_list_012) <= 1:
        return py_list_012
    
    # This initiates the indices for the while loop.
    current_index = 0
    zero_index = 0
    two_index = len(py_list_012) - 1
    
    # The while loop below sorts the list.
    while current_index <= two_index:
        # This creates the current value.
        current_value = py_list_012[current_index]
        if debug_mode:
            print(f'''
            The current index is ({current_index}) and the current value is
            ({current_value}).
            ''')
        
        # If the current value is zero and the current_index and the
        # zero_index are the same, then both indices are updated.
        if (current_value == 0) and (current_index == zero_index):
            if debug_mode:
                print(f'''
                Both the current index and the zero index are equal, and the
                current value is ({current_value}). INCREASING both the zero
                and current indices.
                ''')
            current_index += 1
            zero_index += 1
            continue
        
        # If the current value is zero and the current_index is ahead of
        # the zero_index, the values at the current and zero indices are
        # switched and the zero index is updated (+1).
        if (current_value == 0) and (current_index > zero_index):
            if debug_mode:
                print(f'''
                The current value is ({current_value}). PLACING the current
                value at the zero_index point and then ADDING 1 to the zero
                index.
                ''')
            py_list_012[current_index] = py_list_012[zero_index]
            py_list_012[zero_index] = current_value
            zero_index += 1
            continue
        
        # If the current value is 2 and the current_index == two_index,
        # there is nothing to update and the list has been completely 
        # traversed. The loop is broken.
        if (current_value == 2) and (current_index == two_index):
            if debug_mode:
                print(f'''
                The current value is ({current_value}), and we have reached
                the end. Sorting complete and breaking loop!
                ''')
            break
        
        # If the current_value is 2, and current_index < two_index, then
        # the values at each index are switched and the two_index is 
        # updated (-1).
        if (current_value == 2) and (current_index < two_index):
            if debug_mode:
                print(f'''
                The current value is ({current_value}). PLACING the current
                value at the two_index and then SUBTRACTING 1 from the
                two_index.
                ''')
            py_list_012[current_index] = py_list_012[two_index]
            py_list_012[two_index] = current_value
            two_index -=1
            continue
        
        if debug_mode:
            print(f'''
            The current value is ({current_value}). ADDING 1 to the current
            index.
            ''')
        # If the current value is equal to 1, nothing happens and the
        # current_index is updated.
        current_index += 1
        
    return py_list_012

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Below are the three boilerplate Udacity test cases. Each one should print the sorted
# array and "pass".
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Below are two edge cases: The first one has an empty list, the second case has only
# 1 integer in the list. Each one should print the sorted array and "pass".
test_function([])
test_function([2])

# References
# 1. Udacity Data Structures & Algorithms Nanodegree: 3) Basic Algorithms: 2) Sorting Algorithms,
#    15) Sort 0, 1, 2