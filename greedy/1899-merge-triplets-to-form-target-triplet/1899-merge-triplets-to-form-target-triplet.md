**Notes:**

1. The problem asks us to find out whether two or multiple tripliets are merged based on an given algorithm can become the target tripliet. We only need to return True or False.
2. The first step is to clear our mind thinking about actually merging the triplets and see if that exercise is successful No backtracking or subsets. So we only need to check for patterns here that how triplets are merged what are the requirements. The given algorithm takes the maximum of two values at same indices in both the triplets and either stores or updates the same index of the new triplet. We only need to find out where such kind of merge between triplets results in the target or not.
3. Since given merge algorithm is based on maximum. We should check two thing:
   1. compare each value at index i in triplets with the target triplet. If any value is bigger that the target triplet, we disregard that triplet altogether.
   2. for the remaining triplets, we compare each value at index i of a remaining triplet wth the target triplet and if the value is equal to the target's value, if means we have found a solution for this index.
   3. After that we only have to check whether we found a solution for every index from the remaining triplets.
4. ProTip: We need to keep a Hashset where we would store the indices of the target, whoose solution is found. By the end of the algorithm we just need to check whether we found the soluton for all three values in the traget triplet.
5. ProTip: Loop over the triplets list once and for each triplet, check value all three 0,1,2 indices is greater than the target values. If any value is greater disregard the current triplet and continue to the next triplet. Once a triplet whose all values at indices are smaller than target. Check for each index whether the value is same or not. If the value is same it means this value will the maximum and we have found the solution for this index. so we add this index to the Hashset.
