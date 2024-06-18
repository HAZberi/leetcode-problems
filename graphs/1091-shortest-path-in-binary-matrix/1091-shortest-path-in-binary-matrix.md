**Notes:**

1. The problem asks us to find the shortest path in a given `n x n` matrix, starting from the top left and ending at the bottom right cell. We can move in 8 directions from a given cell. Meaning we can move up, down, left, right and in all 4 diagnal cells.
2. Since we are required to find the shortest path, we will be using the breadth first search algorithm for matrices.
3. For BFS. We need the following infromation:
   1. Length of rows and length of columns in the matrix. It will help us in identifying the bounds of input matrix. In this case length of rows and columns is the same because the given matrix is `n x n`
   2. We need a hashset to store the cells that we have already visited, so we dont need to visit those again.
   3. Since BFS is level by level traversal. We need a queue to store all the cells in current level in a queue before moving on to the next level.
4. We need to check an edge case that whether the first cell is a valid path or not. Meaning the value of the first cell should not be 1. It has to be zero in order to have a valid path. If the value of the top left cell is zero only then we will add it to the queue and the visited hashset. It only means that we have a path length of 1. So we also intialize the length to 1. This is the first level.
5. We keep on running the loop until we there are no values left in the queue.
6. Then we run a for loop till the current length of the queue. At each iteration of this loop we will popleft a single cell from the queue. Then we check whether we have reached our destination cell. The destination cell is `length of rows - 1 and length of cols - 1` . If we have reached the destination we will simply return the length.
7. Now we have to check whether we can move in any of the 8 directions (up, down, left, right and all 4 diagnal cells). The best way to do this is to create a list of direction pairs (row, col), where each pair denotes the position of the neighbouring cell relative to the current cell. `[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]`. ProTIp: Instead of defining these neighbours in this nested loop, we should initialize it globally before the while and for loop. It will marginally save us some run time.
8. Then we check for each direction pair (neighbour) whether the cell is out of bounds or previously visited or blocked. If thats the case then we will simply ignore it by continuing to the next iteration. If we can move to any neightbouring cell then we will add it to the queue and also add it to the visited hashset.
9. Outside this for loop where we process all the cells in the same level. We increment the length by 1 and continue to the next iteration of the while loop.
10. If we reach the destination by doing so then we would have returned the length as mentioned in the step 5. Otherwise we will simply return -1, meaing there is no path between the top left and bottom right cell.

**I have also coded the neetcode solution which is a slight variation of the solution I proposed for a better understanding of myself. But in leetcode my solution run a lot slower than neetcodes solution. Where the main difference is calculating the length and use only 1 loop to add cells to the queue. Neetcode solution is significantly faster. So my recommendation is to always review both solutions and must know the differences between the two.**
