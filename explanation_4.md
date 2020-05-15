# Explanation of Problem_4.py

## Code Design
The sort_012 function works by taking a list of 0s, 1s, and 2s and putting it into a while loop. The current index, the zero index, and two index are tracked. Every time a value in the list equals 1, nothing is done to the value and the current index is updated (+1).  Every time a value in the list equals 0, the values at the current index and the zero index (which is initiated at the beginning of the list) are swapped and the zero index is updated (+1). Every time a value in the list equals 2, the values at the current index and the two index (initiated at the end of the list) are swapped and the two index is updated (-1). The while loop breaks once the current index exceeds the two index.

## Code Efficiency
The merge sort algorithm has a worst-case runtime of O(n log(n)), where n is the length of the input list. The merge sort algorithm has a worst-case space efficiency of O(n) (Reference 1). The function that iterates backwards to create the two numbers has a worst-case runtime of O(n) and a worst-case space complexity of O(1). In total, this algorithm has an overall worst-case runtime of O(n log(n)) and a worst-case space efficiency of O(n) (Reference 1).

## References
1. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms, 2) Sorting Algorithms, 6) Efficiency of Merge Sort