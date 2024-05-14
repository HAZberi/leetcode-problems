**Notes:**

1. The problem asks to find the nodes which are visible to a person standing on the right side of the tree. It is important remember here that, we just dont need to only find the nodes on the right side of the tree. What if both left and right nodes are empty on the right side. Then the visible node from the right will actually be at the left side of the tree. A dfs solution exist, but it will be too complicated. We will use a BFS in this case and take the rightmost node at each level and append it to our result.
2. For BFS we will have a queue. We populate the queue with the root node if the root node exists. Otherwise we will simply return an empty array.
3. We will also have a result array to store the right most nodes.
4. The outer loop will run until there are no nodes in the queue.
5. Inside the outer loop we will initialize the rightmost node to None. This variable will keep track of the rightmost node at each level.
6. Then we start the inner loop which popleft all the values at this current level from left to right. At each popleft we will store the node as the rightmost. Then we will check if this current node has a left child. If yes, we will append the left child in the queue. Then we will check if this current node has a right child. If yes we will append the right child in the queue.
7. Once we exit the inner loop, we append the rightmost node in our result.
8. The time complexity of this solution is O(n) since we go through all the nodes once and space complexity is also O(n) because we are using a queue.
