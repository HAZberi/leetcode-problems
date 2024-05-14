**Notes:** 

1. The problem ask us to find the length of longest substring with unique characters.
2. The brute force approach suggest that we find all the substrings and keep the longest counter. This would be O(n^2) solution.
3. The better way of solving is to use a sliding window with a hashset.
4. Our left pointer starts at zero while our right pointer iterates over the entire array. We need a hashset, this will be used to identify if a character is already present in our current window.
5. We will add characters which are at the right pointer and calculate the max of current length of window (`R - L + 1`) and previous longest length.
6. Before step 5. We have to keep on checking if the charcter at the right pointer already exists in the hashset. If the character at the right pointer exists, then we keep on removing the character at the left pointer and also incrementing the left pointer by one until the character at the right pointer no longer exists in the hashset.
7. Return the longest.
