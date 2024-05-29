**Notes:**

1. The problem ask us to find the k number of closest points to the origin. The points are given in a list. We have to return the points whose distance is closest to the origin.
2. The idea is to basically calculate the distance of each point from the origin. Given is the eculidean distance formula. Then we have two options either we can sort the points by distance which a O(n.logn) operation or we can build a min heap. Building a heap is O(n) operation but then poping value from the minheap is O(logn) operation and we have to pop k times, which mean the time complexity is a bit better than O(n.logn) which O(k.logn) in this case.
3. The question is how to either sort or build heap based on the distance between points and retain all the information without using any extra data structures. For each point we calculate the distance from origin. Note that we dont need to take the square root value, just the square is enough becuase we only need the distance information to compare. So a number without the square root is suffice. (`x - 0)**2 + (y - 0)**2 => x**2 + y**2`.
4. Once we have calculated the distance then we add the distance at 0 index, x at 1 index and y at 2 index in a list. We will do this for each point and create a list of points with their distances.
5. Now we heapify this list as a minHeap. By default python uses the first value to make comparisons.
6. After that we only need to pop from the minHeap k times and append the x,y point pairs to the resultant list. We can run a while loop till k is zero. Pop min value from the heap, append the points to the resultant list and then decrement k by 1.
7. Finally simply return the resultant list.
