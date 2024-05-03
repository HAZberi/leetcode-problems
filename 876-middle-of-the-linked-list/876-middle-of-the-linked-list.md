**Notes:** 

1. The brute force approach of this problem is to calculate the length of the linklist by maintaing a length variable and incrementing it as we visit each next node. Then loop the linklist again till length / 2 and return the middle node.
2. But we have a better approach for this problem. It's called slow and fast pointers.
3. We set both slow and fast pointers to the head of the linklist.
4. Then we keep on moving the pointer until fast pointer and the next of fast pointer are not null. We move the fast pointer by 2*next and the slow pointer by 1*next. By the time this loop finishes, the slow pointer will be at the middle of the linklist. Return the slow pointer.
