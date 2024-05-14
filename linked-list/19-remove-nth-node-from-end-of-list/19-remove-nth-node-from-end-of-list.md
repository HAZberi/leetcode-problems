**Notes:**

1. The most basic and brute force of approach of solving this problem is to reverse the list. Then iterate till n and keep a prev pointer. Then just simply set the prev pointer next to next of current. Then simply reverse the list back again and return the head.
2. The more efficient technique comes from the concept of slow and fast pointer. Here, we will also have two pointers but they will be moving at the same pace and the distance between them remains the same. This distance will be n. Once the forward pointer reaches null, the other pointer will be exactly at the same location that we are looking to delete.
3. If we are at the node, which we need to delete, it a bit difficult to make a connection from the prev node to the next node. In that case we have to keep one more pointer which run one node behind our backward pointer. So its best to introduce a dummy node right at the start and set its next to the head of the list. We start our left pointer from dummy node. The right pointer will n spaces/nodes from the head. We have to use a while loop to assign the starting position of the right pointer.
4. After that we run a while loop until our right pointer reaches to null. At this point our left pointer is just one node behind from the node which we are looking to delete. This is perfect and easy to delete the next node.
5. In order delete the node, we simple set the next of left to the next of next of left.
6. It is importatnt to remeber that we have to return the next of dummy, because thats where the head is.
