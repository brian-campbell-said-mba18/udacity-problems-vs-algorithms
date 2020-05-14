# Explanation of Problem_3.py

## Code Design
The merge sort algorithm is used to sort the python list that contains the digits in the range of (0,9) inclusive. Once the list is sorted, the two numbers are built by iterating
backwards through the list.

## Code Efficiency
The merge sort algorithm has a worst-case runtime of O(n log(n)), where n is the length of the input list. The merge sort algorithm has a worst-case space efficiency of O(n) (Reference 1). The function that iterates backwards to create the two numbers has a worst-case runtime of O(n) and a worst-case space complexity of O(1). In total, this algorithm has an overall worst-case runtime of O(n log(n)) and a worst-case space efficiency of O(n) (Reference 1).

## References
1. Udacity Data Structures & Algorithms Nanodegree; 3) Basic Algorithms, 2) Sorting Algorithms, 6) Efficiency of Merge Sort