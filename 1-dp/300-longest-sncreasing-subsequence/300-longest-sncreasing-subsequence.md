**Notes:**

1. The problem asks us to find the longest increasing subsequence in a given list of numbers. A subsequence is a contigious or non-contigious subset of a list where all the elements are in the same order as they appear in the orginal list. In this problem we looking for the longest subsequence that is increasing.
2. The brute force way of solving this problem is to calculate all the possible subsequences. At each element we have two choice: either to include it n the sequence or not include. Each element having 2 choices and the total number of elements is n. Then we have an esitimated time complexity for this approach will in the order of O(2^n).
3. The second approach is DFS + Caching approach, where we can build a decision tree. We have all the elements taken as a single sequence, i.e each element at index i is start of a sequence. Then for each index, we have a choice to take an element from all the remaining indices to include that in our sequence. At this point we have to make sure that element at the previous index must be smaller than the current index we are considering to make a sequence. We keep on continuing this till we have no more elements to add. We can make use of caching here, since we are calculating the length of sequence at each index, we can use a cache and store. Once we have cached the length of increasing sequence of an index we can use it as is while calculate it elsewhere.
4. Now we will convert this top down approach to bottom up approach by looking from the end of the numbers list. We know all the elements itself are start of a sequence, so we can initialize our dp array equal to the length of the list with 1. Then lets look at the last element, since there are no elements after the last element, we keep the length of sequence at this index as 1. Then we look at the second last sequence, there is one element after it, so longest subsequence at this index is the maximum of itself (which is 1) and 1 + the length of sequence of all the forward remaining indices (which is 1 in this case). We can only look to add elements to sequence if the value at current index i is less than value at any of forward remaining indices.
5. So the longest increasing subsequence at current index = max(itself, 1 + longest increasing subsequence of all the forward remaining indices).
6. Once we break out of the nested loop. We return the maximum of the dp array since it has longest increasing subsequences at every index.
7. The time complextiy of this algorithm is O(n ^ 2) and space complexity is O(n).