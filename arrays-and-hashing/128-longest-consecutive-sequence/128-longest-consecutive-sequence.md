**Notes:**

1. The most important part of find the longest consecutive sequence is to find that what is a sequence and how it starts. When a sequence starts, it has no left neighbour.
2. We can use a HashSet to store all the values of the given input array. Then iterate throught the given array and check whether it has a left neightbour using the hashset. If the number has no neighbours, it means its the start of the sequence so we can then start counting the length of the sequence. We keep on checking the right neighbours and incrementing the length until there are no right neighbours.
3. We should also keep a variable that stores only the max length of the sequence. Pro Tip: use max function to get the max between previous longest sequence and the current length of the sequence.
4. The time complexity of this algorithm is O(n) since we have to go through all the elements in the given input array at most two times. However the space complexity is also O(n) because we are using HashSet.
