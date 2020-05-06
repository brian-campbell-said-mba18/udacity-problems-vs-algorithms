def sqrt(number):
    '''
    Function Purpose: The purpose of this function is to find the square root rounded down to the
        nearest integer for a number, the argument.
        
        Argument: An integer value greater than or equal to 0, AKA number.
        
        Returns: The square root rounded down to the nearest integer.
    '''
    # These assertion errors assert that the argument, number is both greater than or equal to 0
    # and that the number is an interger.
    assert type(number) == int, "The value must be an integer"
    assert number >= 0, "The number must be greater than or equal to 0"
    
    
    # If the number is 0, return 0.
    if number == 0:
        return 0
    # If the number is greater than or equal to 1 but less than 4, return 1.
    if (number >= 1) and (number < 4):
        return 1
    
    # This finds a fraction of the range of 0 to n (the number) to search for the square root. 
    # Only the square root of four is equal to half of the number it is a square root of. Any
    # number greater than four will have a square root less than its median.
    # This while loop starts with the median, upper, and the first quartile, lower. While
    # both upper^2 and lower^2 are greater than the number, the while loop keeps going, dividing
    # upper and lower by 2 after each iteration. Once lower^2 is less than or equal to the number, the 
    # while loop breaks.
    upper = number // 2
    lower = upper // 2
    while upper**2 > number:
        if lower**2 <= number:
            break
        upper = lower
        lower = upper // 2
    
    # If the number == 4, the square root will be upper, the median.
    if upper**2 == number:
        return upper
    
    # If the square root is lower, lower is returned.
    if lower**2 == number:
        return lower
    
    # If upper and lower are not the square root, then a list is created, possible_sqrts, that
    # include all number from range[lower, upper] inclusively.
    possible_sqrts = []
    for i in range (lower, upper + 1, 1):
        possible_sqrts.append(i)
    
    # The while loop below starts with the very last item in the possible_sqrts list and works
    # backwards until the possible_answer^2 is not > the target number.
    the_slice = -1
    possible_answer = possible_sqrts[the_slice]
    while possible_answer**2 > number:
        the_slice -= 1
        possible_answer = possible_sqrts[the_slice]
    
    # Once the while loop breaks, the answer is returned.
    return possible_answer

# These are cases provided by Udacity. Each one should print "pass".
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# This is an edge case that seeks to find the square root of 1 trillion. This edge case does take 
# some time, but still computes in O(log(n)) time.
edge_1 = sqrt(1000000000000)
print(edge_1) # This should be 1000000
print(edge_1**2) # This should be 1000000000000, exactly 1 trillion.

# This is an edge case in which I try to find the square root of "None". An assertion error is
# raised because only integers can be entered as arguments.
sqrt(None)

