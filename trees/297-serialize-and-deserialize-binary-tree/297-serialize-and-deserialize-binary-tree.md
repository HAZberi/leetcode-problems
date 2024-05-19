**Notes:**

1. The problem ask us to convert a tree into a linear structure(list or string) and then converts this linear structure back to tree. I have done a personal algorithm following bfs for testing tree problems.
2. Here we will use preorder dfs to serialize and deserialize the tree. We will serialize the tree into a string and deserialize the string back to a tree.
3. For our serialize method, we will created a resultant array, we will keep on appending values to the array as we traverse the tree and then outside the function we will join the array with a comma delimeter.
   1. So our recursive function will take the root as the argument.
   2. Our base case is whenever we hit a null node, we will append the letter "N" to our resultant array and then simply return None.
   3. If we have a node, then we will append the str value of node value in our resultant array.
   4. Then we recursively call this function on left of root and right of root.
   5. We dont have to return anything, once we have gone through all the nodes, we will have all the string values in our resultant array.
4. For our deserialize method, we will first split the string into values. Then inorder to reach the end of the values list, we need an iterator to take us to the next value in our preorder recursive dfs approach. So we will create a class level variable i and initialize it with zero.
   1. Our recursive function will not take any arguments because we will increment the iterator before any return statements and will be moved on to the next value.
   2. Our base case is whenever we hit a value equal to the letter "N", we increment the iterator and return None.
   3. The we will simply create a TreeNode with integer value of string.
   4. Then we increment the iterator.
   5. After that we recursively call this function to set the left of root and right of root.
   6. And at last we will simply return the root. Also return the ouside method by simply calling this recursive function.
