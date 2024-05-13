**Notes:**

1. The problem asks us to create lists of all the levels in a binary tree. This problem can be tackled with the breadth first search algorithm and appending levels list to the resultant list.
2. For breadth first search we have to have a queue, whick keeps trak of the nodes in one level. We also need a resultant list.
3. We check first if we dont have a root. We simply return an empty list.
4. Then we put the root node in the queue.
5. Then we start a while loop, which basically track the level we are at. This loop will keep on running until there are no values left in the queue.
6. After this outer loop we initialize our level list which will contain all the nodes in the current level.
7. The we start an inner for loop, that runs till the current length of queue. Inside this loop we first pop left a node. Append it to the level list. Then we check if this node has a left child. If yes, we append the left child to the queue. Then we check if this node has a right child. If yes we append the right child to the queue.
8. Once the for loop exits. We append the level list to our result. An then move on to the next iteration of the outer loop. And continue the same process.
9. At the end return the result.
10. The time complexity of this solution is O(n) and the space complexity is also O(n) since we are using a queue.
