**Notes:**

1. The algorithm to solve this problem is very similar to Leetcode 200 - Number of Islands. We used breadth first seach algorithm to use that question, for this question we will discuss the depth first search algorithm and will only write the coding implementation of breath first search algorithm. The underlying intution and approach is exactly the same, only the way we output the result is distinct.
2. The most important thing to solve this question is that contigous cells of 1 represents an island. So basically we traverse the entire matrix m x n. And each cell we check two things.
   1. Whether the cell is an island or not.
   2. Whether we have visited this cell before or not. Because a visited cell can be part of this island itself or it could be part another island. Thats why we have use a top hashset (visited) to keep track all the island cells that we have visited or processed before.
3. Our output is the area of the biggest island. So we initialize an area variable and for each island we traverse with the dfs or bfs algo. We update the max area. At last we simply return the area.
4. While going over the given matrix in the nested loop, as soon as we encounter an island cell that has not visited before. We run either bfs or dfs on that cell. We have to make sure that our bfs or dfs helper function must return area of the island.
5. For our dfs helper method, we pass the current cell's row and column index. The first this we check whether the current cell is in the bounds of our given matrix, also its not in the (visited) hashset and also it's value should not be equal to 0, which represents water. If its not a valid island cell, we will simply return 0. This will be our base case.
6. Now we have to handle the recursive case. First, after the base case, we have a valid island cell, so we add this cell to our visited hashset, so we can ignore this cell, if we encounter this cell again. Second, since 1 valid island cell means the current area of this island is 1. So we initiate the area equal to 1. Then we have to recursively run the dfs on all of the four neighbouring cells and keep on adding the results from all four neighbours to the area. Finally, we simply return the area.