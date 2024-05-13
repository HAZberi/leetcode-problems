**Notes:**

1. This problem asks us to find whether a given tree is a subtree of another tree. One thing is for sure that we have to check each node and compare it with the subroot tree. But how can we do it recursively?
2. The most important thing to solve this question is to know if given roots, can we find both trees are same or not. Yes, absolutely. Leetcode question 100. Exactly tells us whether two tree are similar or not. We know finding same tree is our subproblem here. So we can use the exact same algorithm we used in question 100 as a helper function.
3. So basically, now we know if given two nodes/roots we can find whether trees are same or not. But the problem asks us whether the given tree is a subtree. It means we have to traverse the main tree node by node. We can do it recursively. A right subtree OR a left subtree, either one of the subtrees of the given tree can be equal to given subtree.
4. The most important thing for this problem to solve now, is to clearly identity edge cases, which will also act as the base cases for both our helper sametree function and our main isSubtree function.
5. Edge Cases/Base Case for Helper Method isSameTree:
   1. If both roots/nodes are null => return True
   2. If either one of the roots/nodes are null OR the value of two root/nodes is not equal => return False
6. Edge Cases/Base Case for Main Function isSubtree:
   1. If subroot is null then we return True. Because main tree has null values at the leaf nodes.
   2. If we have the subroot tree but we dont have the root tree. Then we return false.
   3. If the current root/node tree and the subroot tree is equal we return true.
7. The recursive case of the main fuction is checking left subtree is equal OR right subtree is equal and then we return the result.
