def sqrt(number):
    '''
    Function Purpose: The purpose of this function is to find the square root rounded down to the
        nearest integer for a number, the argument.
        
        Argument: An integer value greater than or equal to 0, AKA number.
        
        Returns: The square root rounded down to the nearest integer.
    '''
    # These assertion errors assert that the argument, number is both greater than or equal to 0
    # and that the number is an interger.
    assert number >= 0, "The number must be greater than or equal to 0"
    assert type(number) == int, "The number must be an integer"
    
    # For a number == 1, this conditional returns its square root with a runtime of
    # O(1).
    if number == 1:
        return number
    
    # For any integers greater than 1, this while loop returns the square root value in
    # O(log(n)) time, were n is defined as the range of the number from 0 to n inclusive.
    # First an approximation of the median of the number is found, the query, and a while loop
    # begins. If the query squared is greater than the number, then 1 is subtracted from they query,
    # and the while loop resumes. Once the query squared is less than the number, the query
    # is returned.
    query = number // 2
    while query**2 > number:
        query -= 1
    return query

# These are cases provided by Udacity. Each one should print "pass".
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# This is an edge case that seeks to find the square root of 1 billion. This edge case does take 
# some time. As n gets closer to infinity the runtime becomes closer to O(n/2), but is still
# O(log(n)).
edge_1 = sqrt(1000000000)
print(edge_1) # This should be 31622.
print(edge_1**2) # This should be 999950884.
print((edge_1+1)**2) # This should be over 1 billion, showing that edge_1 is correct.

# This is an edge case in which I try to find the square root of "None". An assertion error is
# raised.
sqrt(None)
