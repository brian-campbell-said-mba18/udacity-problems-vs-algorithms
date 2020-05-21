# Explanation of Problem_7.py

## Code Design
There are two functions of the Router Class, add_handler() and lookup() that are used in Problem_7.py. Add_handler calls upon a function from the RouteTrie class, insert_fullpath(), which uses a for loop to iterate through each part of the path in a full path and insert a node for each path part. At the very last node, the handler is added. The lookup() function is similar in that it calls upon a function from RouteTrie, find_handler(). Find_handler() uses a for loop to traverse through each path part of a full path, and it returns the final node's handler.

## Code Efficiency
The add_handler() function has a worst-case runtime of O(n), where n is defined as every
path part in a full path, due to its use of a for loop. The lookup() has the same worst-case runtime of O(n), because it also uses a for loop. The Router Class has a worst-case space complexity of O(n), because for every path parcel, a node is inserted.

