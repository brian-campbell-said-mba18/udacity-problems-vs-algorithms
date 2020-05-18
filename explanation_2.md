# Explanation of Problem_4.py

## Code Design
In a rotated sorted array, if it is split in half, at least one half will always be sorted. Furthermore, if the unsorted half is split in half, at least one half will be sorted. The function takes a rotated sorted array, identifies a sorted half, and performs binary searches on the sorted half. If the algorithm fails to find the searched for value in the sorted half of the array, the algorithm recursively calls itself, splits the unsorted half in half and binary searches the newly created sorted half. The recursion continues until it examines an array with only one value in it and determines whether the last item is the queried value.

## Code Efficiency
The overall worst-case runtime of the algorithm is O(log(n)), where n is defined as the length of the input array. The algorithm identifies the sorted half in constant time O(n). It then searches the sorted half of the algorithm in O(log(n)) time. Even though the algorithm recurses, every step within the recursive function deals in constant or n(log(n)) runtime. The worst-case space complexity of the algorithm is O(1), because no new data structure was created for the algorithm.

## References
1. Udacity Data Structures & Algorithms Nanodegree: 3) Basic Algorithms: 1) Basic Algorithms, 2) Efficiency of Binary Search
