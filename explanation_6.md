# Explanation of Problem_6.py

## Code Design
This code iterates through a list. It sets the minimum and maximum values to the first value in the list. It then iterates through the rest of the list, updating the minimum and maximum values. Finally, it returns the minimum and maximum values in the tuple format: (minimum, maximum).

## Code Efficiency
This code has a worst-case runtime of O(n), in which n is the length of the list. The code uses a for loop and for each iteration in the for loop, it performs functions that take constant time, IE using conditional statements to check for and record minimum and maximum values. The code has a worst-case space complexity of O(1), because only two values are ever stored, the minimum and the maximum values.