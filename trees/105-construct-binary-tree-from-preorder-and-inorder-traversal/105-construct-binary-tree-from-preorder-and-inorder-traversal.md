**Notes:**

1. The problem asks to create a binary tree from two given lists of preorder and inorder traversals. It means, if we are given a preorder list and an inorder list we have all the information to construct that tree whose preorder and inorder traversals are given.
2. In order to solve this problem we have to rely on the properties of preorder and inorder traversals. In preorder, we process the root first and then process the left subtree and then process the right subtree. In inorder, we process the entire left subtree first and then process the root and then process the right subtree.
3. So this probelm can be solved by breaking up this problem into subproblems and then solve these subproblems recursively. But the question is how should we resolve this problem into sub problem.
4. First we have to define a subproblem. In tree subproblems are generally goes like this. The root, whats at left of root and whats at right of root. We have to follow the same rule.
5. We know the that the first value in the preorder list is the root of our tree. We can find this root value in the inorder list as well. We will be able to extract the index location of the root value in the inorder list. So according to the inorder traversal properties, all the values on the left of this index (mid) in the inorder list are the part of the left subtree and all the values on the right of this index in the inorder list are part of the right subtree.
6. So our recursive case will basically partition the preorder and inorder lists.
7. Our base case is if either of inorder or preorder lists are empty. We dont have enough information to construct the tree, so we will simply return null.
8. Then we take the first element of the preorder list and make it our root node. First element in the preorder list is always the root of that tree.
9. Then we extract index of this root value in the inorder list. We can call this `mid` since it divides the left and right side of our tree.
10. Then we set the left of root (basically the left subtree of the final tree) by recursively calling this method and providing the slice of preorder list `1:mid +1` (in python last value is exclusive) which is basically the number nodes in the left subtree and providing the slice of inorder list `:mid`, basically all the nodes to the left.
11. Then we set the right of root (basically the right subtree of the final tree) by recursively calling this method and providing the slice of preorder list `mid + 1:` which is basically the number of nodes in the right subtree and providing the slice of inorder list `mid + 1:` basically all the nodes to the right. 
12. baFinally we return the root.
