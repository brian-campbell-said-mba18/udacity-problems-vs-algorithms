# Explanation of Problem_5.ipynb

## Code Design
Suffixes() returns all the suffixes that form a complete word, given a prefix. It iterates through all the suffixes recursively. Through each iteration, it adds the suffix to a set if the suffix forms a word. Once the iteration is complete, the set is then converted to a list. The list is then sorted and returned.

## Code Efficiency
Overall, Suffixes() has an overall worst-case runtime of O(n log(n)), where n is defined as all suffixes for a given prefix. Iterating through all the suffixes and adding them to a set takes a worst-case runtime of O(n). Converting the set to a list has a worst-case runtime of O(n) (Reference 1). Finally, sorting the list has a worst-case runtime of O(n log(n)), making the overall worst-case runtime O(n log(n)) (Reference 2). The worst-case space complexity is O(n). Two structures are created with worst-case space complexities of O(n), the set and the list, which makes the overall worst-case space complexity O(n).

## References
1. https://stackoverflow.com/questions/38986244/running-time-for-converting-list-to-set-in-python
2. https://wiki.python.org/moin/TimeComplexity

