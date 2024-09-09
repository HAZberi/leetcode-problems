**Notes:**

1. The problem asks us to create a data structure such that when we provide a point, it can add the point to the data structure and also if we provide a point, it also calculate how many squares this query point can form with existing points in the data structure.
2. There are two important aspects for solving this question.
3. First, we have to check whether a diagnal of the square exists between the query point and any other point in the data set. This will be a linear operation. O(n). So when we add the points, we have to add the points in a list. Now the question is how to find out that whether a diagnal of the square exists between two points. The absolute difference of coordinates is zero. If the conditions satisfies then we will check the remaining two points, whether those two points exist in the data.

   ```
   |x1 - x2| - |y1 - y2| = 0
   |x1 - x2| = |y1 - y2| 
   ```
4. Secondly, if we have duplicate copies of the points then we can form squares equal to the number of copies, but if we have 2 duplicate copies of one point and 3 duplicate copies of a second point. **Then the total number of squares is the product of the copies of these two points**. It is important to note that these two points are not the diagnal. We have to figure out whether any point in the existing data set makes the  square of the diagnal.
5. We would also need a hashmap to count frequencies of the points. Because thats how we can calculate the total number of squares that can be formed with a given point in the diagonal. So we need both list and a hashmap. List will store all the duplicates while hashmap will have the frequencies and it will also give us.O(1) access when we need calculate the product of copies of two remaining points.
6. How to find remaining points. If a diagonal exists between two point. Then consider the following to find the points and check the frequency map for existance of these points in O(1)

   ```
   Diagonal Point (x, y)
   Query Point (px, py)

   Remaining point 1 r1(px, y)
   Remaining point 2 r2(x, py)
   ```
7. The time complexity of count method is O(n) and the space complexity is also O(2n). Since we need a list and a map as well.
