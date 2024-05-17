**Notes** 

1. The problem ask us to find the k smallest node, meaning k=1 is the smallest node in the tree. k=2 is the second most smallest node in the tree. k=3 is the third most smallest node in the tree and so on.
2. The best algorithm that traverses the tree such that we have all the nodes processed in ascending order. We can use either recursive inorder dfs or iterative inorder dfs.
3. For the recursive dfs we put all the values in an array, in the ascending order and then get the kth node at k-1 index in the array and return it. But we have to go over the entire tree before we get the kth smallest.
4. The idea of iterative dfs is the we keep on counting the nodes when we process them, as soon as our number of nodes processed becomes equal to the value k. We return the value at that node.
5. So, we need a variable to keep the count of currently processed nodes. We also need a stack to store the values before we process them.
6. Then we run a loop till current node or the stack are not empty. If the current node exits, we append it to the stack first. Then we go to the left by updating the current node to its left child. If we reach a current node that is null, We pop out the element from the stack and make it the current node. We also increament the counter by 1. And after that check whether count of nodes becomes equal to the value of k. If yes, then we simply return the value of the node. We are guaranteed to find a solution. Now we have processessed the node. Now we update the current by assinging to the right child.
7. We dont have to return anything here.
