def bin_search_helper(arr, target, beg, end):
    '''
    Helper Function Purpose: This helper function searches for a target 
        number in an sorted array. If the target number is found, the
        function returns the index in which it was found. Otherwise, it
        returns -1. Note, this helper function is a recursive function.
        
    Arguments: Arr = the array to search in. Target = the number that is
        querried. Beg = the beginning index. End = the end index.
        
    Returns: The index of the target number, or -1 if the target number is
        not in the array.
    '''
    # This is a base case in which there is only one element in the array.
    # If the target is found, then the index is returned. Otherwise, -1 
    # is returned.
    if beg >= end:
        if target == arr[beg]:
            return beg
        else:
            return -1
    
    # This initiates the midpoint variable to be used for the recursive
    # functions below.
    midpoint = (beg + end) // 2
    
    # This is another base case, if the target is at the midpoint of the
    # array, we return the midpoint index.
    if target == arr[midpoint]:
        return midpoint
    
    # This is the first recursive case. If the target is less than the 
    # midpoint value, we recurse the half of the array below the midpoint 
    # index.
    if target < arr[midpoint]:
        return bin_search_helper(arr, target, beg, midpoint - 1)
    
    # This is the first recursive case. If the target is greater than the 
    # midpoint value, we recurse the half of the array above the midpoint 
    # index.
    if target > arr[midpoint]:
        return bin_search_helper(arr, target, midpoint + 1, end)

def left_right_bin_helper(the_array, the_target, beg_ind, end_ind):
    '''
    Helper Function Purpose: The purpose of this function is to split a
        rotated array into two halves, a lower and upper half. This
        function identifies which half is sorted, and performs a binary
        search on that half. The binary search identifies whether
        the target number, the_taret, is in the half of the array. If
        the_target is not found, this function recursively calls itself.
    
    Arguments: The_array = the array that the_target is searched in.
        The_target = the qurried number that is searched for in the_array.
        Beg_index = the beginning index of the search.
        End_index = the end index of the search.
        
    Returns: If the_target is in the_array, the index of the target value
        is returned. Otherwise, -1 is returned.
    '''
    
    # This is the base case. If there is only one item in the array, this
    # value is querried to determine whether the target exists within the
    # array.
    
    if beg_ind >= end_ind:
        if the_array[beg_ind] == the_target:
            return beg_ind
        else:
            return -1
    
    # This initiates the median value. This is an estimate.
    median = (beg_ind + end_ind) // 2
    
    
    # If the bottom half of the array is sorted, then a binary search is
    # performed on the bottom half. If the target value is found, then
    # the index is returned. Otherwise, this function is recursively called
    # to examine the top half of the array.
    if the_array[beg_ind] < the_array[median]:
        output = bin_search_helper(the_array, the_target, beg_ind, median)
        if output != -1:
            return output
        else:
            return left_right_bin_helper(the_array, the_target, 
                                         median + 1, end_ind)
    
    # If the bottom half of the array is not sorted, then a binary search
    # is performed on the top half. If the target value is found, then
    # the index is returned. Otherwise, this function is recursively called
    # to examine the bottom half of the array.
    if the_array[beg_ind] >= the_array[median]:
        output = bin_search_helper(the_array, the_target, median + 1, 
                                  end_ind)
        if output != -1:
            return output
        else:
            return left_right_bin_helper(the_array, the_target, beg_ind,
                                        median)
            
def rotated_array_search(input_arr, target_num):
    '''
    Function Purpose: The purpose of this function is to identify whether
        a target number, target_num, is within an array, input_array. If it
        is, this function returns the index in which the target number can
        be found. Otherwise, -1 is returned. This function uses the 
        assistance of a helper function, left_right_bin_helper, to perform
        the query.
    
    Arguments: Input_arr = the array in which target_num is searched in.
        Target_num = the target num that is searched for in input_arr.
    '''
    # In the case that there is nothing in the input array, this function
    # returns -1.
    if len(input_arr) == 0:
        return -1
    
    # This initiates the beginning and end index variables reqired for
    # the left_right_bin_helper to perform the search.
    first_index = 0
    last_index = len(input_arr) - 1
    
    # This executes the search using left_right_bin_helper.
    return left_right_bin_helper(input_arr, target_num, first_index,
                                 last_index)

def linear_search(input_list, number):
    '''
    Function Purpose: This is a boilerplate function provided by Udacity.
        It searches for a value within an array in linear time.
        
    Reference: Reference 1 of References.
    '''
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    '''
    Function Purpose: This is a boilerplate function provided by Udacity. It
        compares the answers of rotated_array_search function to the 
        linear_search function. If the answers equal each other, the
        rotated_array_search fucntion passed, and "pass" is printed.
        Otherwise, the rotated_array_search function failed and "fail" is
        printed.
        
    Reference: Reference 1 of References.
    '''
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
    
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# REFERENCES:
# 1. Data Structures & Algorithms Nanodegree; 3) Basic Algorithms;
#    4) Problems Vs Algorithms; 3) Problem 2: Search in a Sorted Array.
# 2. Data Structures & Algorithms Nanodegree; 3) Basic Algorithms;
#    1) Basic Algorithms; 3) Binary Search Practice