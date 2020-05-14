def merge_helper(left, right):
    '''
    Helper Function Purpose: This function merges 2 python lists, left
        and right, which contain integer values. This function compares
        values of both lists, and appends them into a sorted list,
        merge_list. This is a helper function for the function merge_sort.
    
    Arguments: Two lists with integer values, left and right. Both the left
        and right list have been sorted before they were put into the
        function.
    
    Returns: A new sorted list, merge_list.
    '''
    merge_list = []
    left_index = 0
    right_index = 0
    
    # This while loop compares integers in the left python list to integers
    # in the right python list. The smaller of the the two integers is
    # appended to the merge_list. The list in which the integer was
    # extracted from has its index updated in order to update the while
    # conditional after each iteration.
    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] < right[right_index]:
            merge_list.append(left[left_index])
            left_index += 1
        else:
            merge_list.append(right[right_index])
            right_index += 1
    
    # Once the while loop is broken, the remaining integers from the
    # python list, right or left, that still has values is appended to
    # the merge_list.
    if left_index < len(left):
        merge_list += left[left_index:]
    else:
        merge_list += right[right_index:]
    
    return merge_list

def merge_sort(arr):
    '''
    Function Purpose: This funciton sorts a 1-dimensional array through
        recursion. The base case returns an array if the length of it is
        <= 1. Otherwise, it continues to break arrays into two separates
        that are eventually sorted and merged through a function called
        merge_helper.
        
    Arguments: arr, an unsorted array.
    
    Returns: The sorted version of arr.
    '''
    # This is the base case.
    if len(arr) <= 1:
        return arr
    
    # This defines the midpoint and left and right arrays to be recursed.
    midpoint = len(arr) // 2
    left_side = arr[:midpoint]
    right_side = arr[midpoint:]
    
    # This is the recursive case, the newly initiated left_side
    # and right_side arrays are recursed. Once both sides have been
    # fully recursed, this function then calls upon the merge_helper
    # function to merge the two arrays.
    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    return merge_helper(left_side, right_side)

def greatest_2_ints(sorted_array):
    '''
    Function Purpose: This takes a sorted list and finds two numbers that
        are within 1 digit of each other in length that maximizes the sum 
        of the two numbers.
        
    Arguments: The sorted array, sorted_array.
    
    Returns: A list of two numbers that are within 1 digit in lenght and
        and their sum is maximized.
    '''
    # This initiates the selection, number1, number2, beg_index, and 
    # end_index variables.
    selection = 1
    beg_index = len(sorted_array) * (-1)
    end_index = -1
    number1 = ""
    number2 = ""
    
    # This while loop starts at the end of the sorted_array, where the
    # greatest digit values are, and appends them to one of the two 
    # numbers number1 or number 2, depending upon the value of the
    # variable, selection (selection changes every time after each
    # iteration to ensure that both numbers are within 1 digit of each
    # other and their sum is maximized).
    while end_index >= beg_index:
        if selection == 1:
            number1 += str(sorted_array[end_index])
            end_index -= 1
            selection = 2
            continue
        
        if selection ==2:
            number2 += str(sorted_array[end_index])
            end_index -= 1
            selection = 1
            continue
    
    return [int(number1), int(number2)]

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 1:
        return 
    
    if len(input_list) == 1:
        return input_list
    # This sorts the input_list of integers. An integer in the list can
    # only be one from the range (0,9) inclusive.
    chronological_list = merge_sort(input_list)
    
    # This returns the two integers that are within 1 digit in length of
    # each other and their sum is maximized.
    return greatest_2_ints(chronological_list)
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if len(test_case[0]) < 1:
        if test_case[0] == test_case[1]:
            print("Pass")
        else:
            print("Fail")
        return
    
    if len(test_case[0]) == 1:
        if test_case[0] == test_case[1]:
            print("Pass")
        else:
            print("Fail")
        return
    
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# This is 1 of 2 of the boilerplate Udacity test cases.
test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1) # This should print "pass".

# This is 2 of 2 of the boilerplate Udacity test cases.
test_case_2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_2) # This should print "pass".

# This is an edge case in which a blank list is the input. The output
# is also a blank list.
test_case_3 = [[], []]
test_function(test_case_3) # This should print "pass".

# This is an edge case in which a single integer is the input. The output
# is that integer.
test_case_4 = [[9], [9]]
test_function(test_case_4) # This should print "pass".