**Notes:** 

1. The problem asks us to find the minimum number of operations required to convert a word1 to word2. We are not allowed to make any changes to the word2. We are only allowed to do 3 different operations (insert, delete, replace) on word1 to make it to exactly same as word2.
2. This problem is a similar problem to longest common subsequence and hence it can be solved with dynamic programming. We know we can implement caching to speed this up, but we have to first find the recursive solution to the problem. This will lead us to reducing the time complexity from O(3 ^ (n + m)) to simply O(n.m) with space complexity of O(n.m) for the cache.
3. Lets analyze the basic and most trivial cases first. In this problem we have quite a few to deal with.
   1. If both word1 and word2 are empty. It means it will take 0 operations in converting word1 to word2. Similary if the character pointer of word1 (i) is at the length of word1 and character pointer of word2 (j) is at the length of the word2. This will also mean that it will take 0 operations to convert word1 to word2. This is our first termination base case.
   2. If length of the word1 is zero or there are no characters in word1, but word2 has characters. We return the length of remaining characters of word2. If word1 was zero, entire length of word2 will be returned. Why? Because it will take the (length of remaining characters) operations to convert word1 to word2. We will insert all the characters or remaining characters from word2.
   3. If length of the word2 is zero of there are no characters in word2, but word1 has characters. We return the length of remaining character of word1. If word2 was zero, entire length of word1 will be returned. Why? Because it will take the (length of remaining characters) operations to convert word1 to word2. We will delete all the characters or remaining characters from word1.
   4. Now lets discuss the recursive cases:
      1. If the charcters at character pointer (i) for word1 and the character pointer (j) for word2 matches, it means we have to do nothing. There will be no operation. And we move both the pointers to (i + 1, j + 1). Moving pointers is basically calling the recursive function. This problem is solved and we add the result of recursive call to operationsCount or cache.
      2. If the charcters at character pointer (i) for word1 and the character pointer (j) for word2 are not matching. Then we will have three chioces of operations to perform. (insert, delete, replace).
         1. If we insert a character from word2 in word1, we will insert it one place before the character pointer (i). So we will not change the (i) pointer but (J) pointer will be moved becasue insertion has cancelled out the current character at (J) pointer. So it will be (i, j + 1).
         2. If we delete a character from word1. Then we have to move the char pointer (i) but we dont need to move the char pointer (j), because when we moved the char pointer (i) we will have a new comparision. So it will (i + 1, j)
         3. If we replace a character, basically changing the the character in word1 at char pointer (i) exactly same as the char pointer (j). Then this comparision is done and we can move both char pointers. So it will be (i + 1, j + 1)
      3. All the above three operations mean that we have done 1 operation, and then we have 3 different choices and from these 3 choices we have to pick the choice that give us the minimum number of operations to convert word1 to word2. So it wil `1 + min((i, j + 1), (i + 1, j), (i + 1, j + 1))`
   5. We can cache all these result for (i,  j) and reduce the runtime complexity by simply looking at the cache right after our first base case. (right after first base case is the best place to check for cache)
4. Lets convert this top down solution to the bottom up tabulation solution. As every bottom up approach in two dimensions, we require a grid. The grid dimensions are m + 1 x n + 1 where m is the length of word1 and n is the length of word2. Why not m x n? Because we have to cater for the base cases, we know when our both character pointers are at the length of thier respective words, we return true. In the table that cell is m x n, so we need 0-m and 0-n all inclusive, thats why the grid dimensions are m + 1, n + 1. We also need to intialize the other base cases as well, when one string is empty and the other string has characters, then we return the length of remaining characters from the other string. Those values will be sequential and in decreasing order starting from 0th index of other string.
5. Now with are dp grid populated correctly, we start teh traversing the grid from the bottom right corner, since we already have values calculated for the base cases. So if a character matches, we look the diagnal cell and take its value. If characters dont match, then we must have to perform an operation and we also have to pick the minimum number of operations taken by (i, j + 1) insertion which is on the right cell and (i + 1, j) deletion which is on the bottom cell and (i + 1, j + 1) replace which is on the diagnal cell.
6. After that we will simply return the first value from the grid at (0, 0).
7. Time complexity is O(n.m) with space complexity of O(n.m) for the grid.