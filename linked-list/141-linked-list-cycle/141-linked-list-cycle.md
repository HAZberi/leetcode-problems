**Notes:**

1. This problem is solved by having a hashset, each value we visit we put in the hashmap. We check our hashmap that if cur node exists in our hashmap and if it does we have a cycle. If not, and we get to the end of the list, we simply return false. This solution is uses space complexity of O(n)
2. The solution that is actually a lot better in terms of space is O(1). It makes use of the slow and fast pointer algorithm.
3. Both slow and fast pointers start at the head of the list. Slow pointer will move one node and fast pointer will move two nodes.
4. Since fast pointer moves fast, we run the pointers till any one of the fast or next of fast becomes null.
5. At any point traversing through the list fast pointer meets the slow pointer. Meaning fast and slow nodes becomes equal we simply return True. Otherwise whenever we get to the end of the list, which is null. We return false.
