**Notes:**

1. This problem asks us to find the maximum elememnt in a sliding window of size k. The output is an array of maximums in all sliding windows.
2. The brute force approch is relitively simple. For each sliding window, we caluculate the max and append it to the output array. But this would be inefficient becuse the its O(k x (n-k)). where k is the size of the window. and (n-k) is how many times a window will move.
3. In order to achieve a linear time solution. We have to eleminate all the redundant work, if we are adding an element to the sliding window, we should just do one comparision to decide whether we have a new maximum or not. Here we need a data structure that can move with our sliding window and values can be added and remove in O(1). We will use a queue. This type of problem is solved by the montonic decreasing queue.
4. We start our siliding window, for each element we check whether the front element of the queue is smaller than the current element. If smaller, we simply pop the queue from front. We keep on doing that till we have an element that is smaller than the element at the front of the queue. At this point we append the index of the current element to the queue.
5. After that check if left pointer is greater than the index stored at left/back of the queue. If is greater than popleft the queue.
6. If the sliding window is equal to the k. Then we append the leftmost value of the queue to the resultant array. Also at this point we increament the left pointer.
7. Return the resultant array.
