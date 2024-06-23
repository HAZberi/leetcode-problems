**Notes:**

1. The problem asks us to find a total unit of time it takes for all the fresh oranges to become rotten. A fresh orange must be 4 directionally adjacent to a rotten orange to become rotten in the next iteration of the time. If there are any fresh oranges still left, which were not 4 directionally adjacent to a rotten orange then we should return -1.
2. The first algorithm we can apply here to solve this problem would be DFS but it wont work. It would only work if there is only one orange rotten in the grid. If there are two or more rotten oranges then we have to go layer by layer starting from each rotten orange. So basically the most appropriate algorthm to solve this problem is multi-source BFS where the given rotten oranges in the grid are the source of BFS.
3. We also need to keep track of the fresh oranges in the grid. It is possible that a fresh orange is not adjacent to any of the rotten oranges. In that case we have to return -1. We also need to keep track of the time. Here time basically represents each level/layer starting from the rotten oranges.
4. The first step is to loop over the entire grid. We should have the bounds of the grid. For each cell traversed we check 2 things:
   1. If its a fresh orange we increment the fresh orange count by 1.
   2. if its a rotten orange we append this cell to the queue.
5. After that we run the standard matrix BFS while loop, usually the while loop terminates whenever the queue is empty but here we will add one more AND condition. The count of fresh oranges should be greater than 0. ProTIP: Doing this will make our loop much tighter and efficient.
6. Then we take a snapshot of the queue and start popping left. Once we pop the cell, we will check its all four neighbours using a loop. If a neighbouring cell is in bounds AND its value is a fresh orange. Then we make this fresh orange a rotten orange. We will also append this cell to the queue. We will also decrement the count of fresh oranges by 1. Then we exit out of both inner loops. And inside the outer while loop we will increment the time by 1.
7. Finally we return the time if there are no fresh oranges left otherwise we will return -1.
