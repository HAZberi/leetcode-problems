**Notes:**

1. This problem is very simple in a sense that it can be easily solved brute force by going through each element in a nested loop. This is will be O(n ^ 2). But the problem requires a solution that runs in atleast O(log(m*n)). The solution we are after, runs O(logm) + O(logn).
2. Binary search is a popular algrorithm that can be used to search elements in an array. The same concept can be applied here as well
3. We know in a matrix we have ROWS and COLUMNS. The two conditions we are given tells us that the ROWS are in ascending order, meaning last value in the previous row is smaller than the first value in the next row. It means we can run a binary search to find which row might have our target value. If we dont find any rows that have the target. We can return false at this point. After just running binary search on the rows.
4. If we end up finding a row that might have our target value. Then we run the binary search just on that row. If we find a value retrun true or false if we dont.
5. ProTip: Use good naming for variables. The same way we visualize the problem. top, bottom for rows. Number of ROWS and COLUMNS.
