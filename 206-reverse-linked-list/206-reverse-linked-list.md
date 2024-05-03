**Notes:**

1. This is a very common interview problem. It can be solved with two approaches. ITerative and recursive.
2. Iterrative Approach
   1. We have two pointers, current which is equal to head and prev pointer which is equal to null initially.
   2. We have to run a loop while current pointer is not null.
   3. Before reversing the current's next pointer to prev we should store a copy of this current'next in a variable nxt.
   4. Now we can set the current'next to prev pointer.
   5. Now we have to move the pointers. prev becomes current and current becomes the node stored in the variable nxt.
   6. Once eveything is done we return the prev pointer. Because the while loop exits when current pointer becomes null.
3. Recursive Approch
   1. Recursive approch means we have to divide into sub problems until we find the most trivial problem. That trivial problem becomes our base case. Here, we keep on calling the function recursively with new heads (head.next). until we reach the end of the list. At that point we start reversing the next pointers.
   2. First, we should return None right away if there is no head.
   3. At this point we have to find our new head, which is basically end of the list. So we set the current head to new head. Then check if next of head exists. If it does then we recursively call this method again and this time head is actually the head next.
   4. Once we hit a head that has no next. We set this next of head to null. At this point our fucntion starts backtracking.
   5. Now we set the next of next of head to head. Reversing the next pointer. Then outside the loop we are setting this current next of head to null.
   6. Finally we return the newhead.
