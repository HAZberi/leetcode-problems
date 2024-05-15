**Notes:**

1. The problem asks us to find the number of good nodes in a binary tree. The good nodes have the largest or equal to the largest value along the path from the root to that node. Root -> Node
2. Starting from root we have to check each node that whether its value is greater or equal to current maximum value in this path. If its greater then we increase the result count by 1 if not then we will increase the count by 0. Then we can update our current maximum.
3. After that we also need to increment the result by counting good nodes in the left subtree and right subtree. This will be our recursive case.
4. The best way to approach this problem is preorder recursive dfs. We process the node first and then process the left subtree and then process the right subtree, then compound the result and return it.
5. Our base case is where the root or current node is null. We return 0.
6. return the result.
7. If a good node, we have 1 + goodNodesOnLeft + goodNodesOnRight. If not a good node, we have 0 + goodNodesOnLeft + goodNodesOnRight.
8. The time complexity of this solution is O(n) because we have to go through each node. But the space complexity is O(logn), because the call stack process all the left nodes first and then all the right nodes. At the max depth of the tree, call stack snapshot will be of (logn) space.
