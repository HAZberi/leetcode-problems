**Notes:**

1. The problem asks us to find a path in a binary tree with maximum sum. The path doesn't necessarliy go through the root. The max sum can have the sum of nodes from both subtrees or only one subtree. We call it the sum with split (both subtrees)  and the sum without split (max of left and right subtrees).
2. The top-down approach to solve this problem involves a lot of repeated work and will result in a time complexity of O(n ^ 2). In this problem we will use a recursive dfs appraoch and recursively solve the problem in bottom up approach.
3. Although this problem can be solved without having a global variable. But in order to keep things easier to understand we will keep a global variable to store the max sum.
4. Here we need to decide what our recursive function will return. For starters it should return a max sum at that node. Now the question is what kind of sum. We have two types of sum that we are calculating here. One is with the split (left sum and right sum) from the parent node . The second is without the split (max of left or right sum) from the parent node. If we are not using a global variable we can return both sums as a list and the outside of the recursive function we can take the max of both sums and return it as the final result. Here we will only return the sum without the split from node. This will also help us in updating the final max sum when we will calculate the sum with the split.
   1. With split `node.val + leftmax + rightmax`
   2. Without the split `node.val + max(leftmax, rightmax)`
5. So our base is if we hit a node that is null. We will simply return 0.
6. Then we need to find the sum of left subtree without the split. So we will call the recursive function on left node. Similarly we need to find the sum of right subtree without the split. So we will call the recursive function on the right node.
7. Since we are calculating the max sum and the node values can also be negative. So we can apply kadanes algorithm here as well. Meaning if the sum of left or right is negative, we can default it to zero before adding the root/node value and returning it.
8. Now we have to update the result max sum. `max(maxSum, node.val + leftmax + rightmax)`
9. The return statement for our recursive function will basically add the current node value to the maximum of leftmax and rightmax. This will be the sum without the split. `node.val + max(leftmax, rightmax)`
10. Outside the recursive fuction we will call the recursive function which update the max sum and then we simply return max sum.
11. Since we are visiting each node only once. So the time complexity of this algorithm is O(n)
