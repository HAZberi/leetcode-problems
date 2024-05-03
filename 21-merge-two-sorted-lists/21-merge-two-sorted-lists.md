**Notes:**

1. In this problem we will merge the two sorted lists by creating a new output list. This output list starts with a dummy node. Dummy node will make the insertion easier since we don't have to check the edge case that whether there is a head or not. So, if we are looking to insert values we should always use a dummy node. We also set this dummy node to tail. Whenever we add a value to the list, we will move the tail pointer as well. The tail pointer always indicates the end of our output list.
2. Now we start a while loop that run till the minimum length out of the two lists. Basically saying that while l1 AND l2 are not null.
3. Then we check if l1 is less than l2. if yes then we set the next of tail to l1 node. Then we move the tail pointer to next of tail.
4. In all other case where l1 >= l2. We set the next of tail to l2 node. Then we move the tail pointer to next of tail.
5. Once we are done from the loop, we will check if l1 exists, then we set the next of tail to l1. Otherwise we will the next of tail to l2.
6. Then simply return the next of dummy.
