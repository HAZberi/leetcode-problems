**Notes:**

1. This problem asks us to ceate a deep copy of linklist whose node as val, next ana random pointer. Random pointer can point to any node in the list.
2. The problem looks simple that we copying the node like we do for a normal linklist and assign random pointers as we go. But we cannot assign random pointer to node that does not even exist at the time of assignment.
3. So, we will do two passes over the list. Also use a hashmap to store old nodes as key and the copy nodes as value.
4. In first pass, we make a copy of node and its value only. Set the old node as key and set its value to current copy created. Then move to the next node.
5. In second pass, we extract the copy node by using the old node's key from the hashmap. Then we set the next of copy by assigning it to the old node's key next of current. And exactly the same way we set the random of copy by assigning it to the old node's key random of current. Then move to the next node.
6. Once everything is done, we return the hashmap key as head.
