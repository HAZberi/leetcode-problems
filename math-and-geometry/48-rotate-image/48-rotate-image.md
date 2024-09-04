**Notes:**

1. The problem asks us to find to rotate a matrix by 90 degrees. We have to perform this operation in place.
2. We can not use an auxiallry space for this problem. So we basically need to find the pattern in which the rotation is happening.
3. Let's analyze how the rotation is happening at the outer most layer of the cells in the matrix. A matrix has a Left Right Top and Bottom cells. We will see that:
   1. The top left value goes to the top right
   2. The top right value goes to the bottom right
   3. The bottom right value goes to the bottom left
   4. The bottom left value goes to the top left.
4. That's how the rotation of corner cells of the the matrix is completed. The corner cells are in the correct spot now. We will notice that these four cells makes a square. Then we move on to the next cell of top left cell. We will see that:
   1. The top left + 1 cell value goes to the right column at row 1.
   2. The right column row1 value goes to 1 offset left from the bottom right.
   3. The 1 offset left from bottom right value goes to the 1 offset up from the bottom left.
   4. The 1 offset up from the bottom left value goes to the top left + 1 cell value.
5. So basically we need to perform n - 1 rotations in a similar fashion, each time increasing the offset by 1 cell up until n - 1 cells. This will complete the outer most sqaure of the matrix.
6. Then we need to update the bounds of the matrix L, R and Top left as well. Such that the inner layer of the matrix is accessible for rotation. We can maintain L and R pointers. Whenever Left crosses the Right pointer or becomes equal, we are done with all the rotations.
7. When we are trying to rotate the and swap the values, we need temporary variable to store the value. At each swap we need a temporary value. For each rotation we will need at least 3 temporary variable. Using so many temp variable will increase the complexity of the program. Can we have a better way. Yes we do. If do the swaps in reverse order.
   1. We save the top left cell in a temp variable and then replace its value with bottom left value.
   2. Then replace the the bottom left value with bottom right value.
   3. Then replace the bottom right value with top right value.
   4. Then finally replace the top right value with top left value stored in the temp variable.
8. Since we have to go over the entire matrix at most once, the time complexity of this algorithm is O(n ^ 2).
