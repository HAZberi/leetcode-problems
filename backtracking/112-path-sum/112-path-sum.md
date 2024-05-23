**Notes:**

1. The problem asks to find the path sums of a given binary tree (not a BST) and check if there is a path sum that is equal to the given target sum.
2. This problem can be solved by recursive preorder dfs which pretty much is the same as the tree maze algorithm.
3. So as majority of dfs solutions we will have an inner recursive function with a node argument. But here we have to calculate the sum of the path. So we have to maintain a variable with the dfs recurision which will have the current sum. So a second argument as currSum.
4. Like all the dfs problems, if there is no root/node, we will simply return False. Since it means there is either a path on the left or the right of this node.
5. If we reach a leaf node, meaning a node with no left child and no right child. Then we compare the currsum with target sum and return the result.
6. Finally we arrive at our recursive call. We wiil check if left child has the target sum OR right child has the target sum. If any of the two condition is true we will return true otherwise we will return False. Basically we can take the OR of two recursive calls.

# class TreeNode:

# def __init__(self, val=0, left=None, right=None):

# self.val = val

# self.left = left

# self.right = right

classSolution:

defhasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
