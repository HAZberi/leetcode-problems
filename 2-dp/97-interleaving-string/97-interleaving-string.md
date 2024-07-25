**Notes:**

1. The problem asks to find whether given strings s1 and s2 forms the string s3. Also if the length of s1 is m and length of s2 is n, then the length of s3 = m + n, otherwise its impossile to make s3. This is an edge case for this problem. We can pick any length of substrings that matches the characters in s3 but the important thing here is that the order cannot be different.
2. Before going into the brute force and memoization appraoch, lets discuss the intuition. We know a solution is only possible whenever the length of s1 and s2 added is equal to the length of s3. Then we make comparision character by character with s3, first with s1 string and then with s2 string.

   1. If the character in s1 matches with the character in s3, we increment the character pointer by 1 in s1 and also in the s3. The character pointer of s3 let's say k = character pointer in s1(i) + character pointer in s2(j). If the character in s2 matches with the character in s3, we increment the character pointer by 1 in s2 and also in the s3. It will be automatic, because instead of keeping track of k, we will just add i + j to get the location of character in s3.
   2. If both of the characters in s1 and s2 dont match with current character in s3 then we will simply return False, concluding that s3 cannot be formed with s1 and s2.
   3. If both of the characters in s1 and s2 matches with the current character in s3 then we will have two choices:

      1. Increment character pointer in s1 by 1 and keeping the character pointer in s2 same.
      2. Increment character pointer in s2 by 1 and keeping the character pointer in s1 same.

      In this case we want to know, whether there is a possiblity of forming s3 from any of these two choices. So basically we can take the OR these two results.
   4. If we get to the end of the strings, meaning both character pointers become equal to the length of their respective strings, then we must return True, because we have found that s1 and s2 can form s3.
3. Now based on these observations, lets discuss the Top Down DP solution. Our base case is whenever we reach end of both strings, as mentioned in the point(4) above. We will return True. Then we will check our cache and return the result from the cache. After that, we check three conditions, remember our DFS method checks whether forming s3 is possible or not. So we can combine this recurisive conditions. So we will check three things for s1 and three things for s2.

   1. First check if the character pointer for s1 is in bounds AND if character pointer for s1 is in bounds then check whether the character matches with the (i + j) character pointer in s3 AND if characters are matching then check if we increment the character pointer for s1 by 1 and keeping the character pointer in s2 the same. Are we able to form a s3 successfully? If Yes then return True, we dont even need to cache it because when we backtrack from here we will simply keep on passing the True till we reach the root.
   2. Then check if the character pointer for s2 is in bounds AND if character pointer for s2 is in bounds then check whether the character matches with the (i + j) character pointer in s3 AND if characters are matching then check if we increment the character pointer for s2 by 1 and keeping the character pointer in s1 the same. Are we able to form a s3 successfully? If Yes then return True, we dont even need to cache it because when we backtrack from here we will simply keep on passing the True till we reach the root.

   If we are unable to satisfy both of the above conditions, then there is only thing left, that character pointers at s1 and s2 both are NOT matching with character pointer at s3. So we will cache this result and simply return False.
