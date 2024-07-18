**Notes:**

1. The problem asks us to partition a given string such that characters in each partition do not appear in any of the other partitions. It's importatnt to note here that we only need to return the lengths of each partition and not the partition itself.
2. The intiution to solve this problem is that each partition contains all the same characters such that the partition remains contigious. So the question is if we have multiple characters, which character is the most important? The last occurrance of the character in the string is most important beacuse it will mean that all the similar characters are part of the current partition.
3. So we need to find all the last indices of the character occurrance. We can use a Hashmap, to store the last index of each character. It will be a simple O(n) operation.
4. Then we need to have find the lengths of each possible partition. We can track the length of each partition in a variable as we iterate through the characters. Once we reach the end of the partition, we add the length of the resultant list and reset the partition length back to zero.
5. Now the question is how do we find the end of the partition. We initialize the end variable to 0. Then for each character, we check the character's last index in our hashmap. If the current index and the character's last index are equal, it means we have found a partition. But before this check, we should update the ending index, we take the maximum of current ending index and the last index of current character. That way when we check current index and character last index to equal we will have the current ending index of the partition.
6. Finally we will simply return the resultant list of lengths.
7. This solution is O(n) and space is O(1) becasue we the size of the hashamp is O(26) at worst, which is constant.
8. This a greedy solution because we only need to keep track of the last index.
