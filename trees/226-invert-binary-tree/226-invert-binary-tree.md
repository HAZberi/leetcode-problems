**Notes:**

1. The problem is basically asking us to swap all the children nodes, meaning swap the left node with the right nodes.
2. This problem can be solved by preorder and postorder DFS. The problem generates a recursive case. So it is better to use the recursive dfs.
3. So first we check the root. if its null, we simply return null.
4. Then if we want to go with the preorder DFS. We swap the left and right nodes of the root.
5. Then we simply recursively call the invert binary on the left and right nodes.
6. At the end we simply return the root.
