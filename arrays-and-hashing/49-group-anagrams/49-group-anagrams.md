**Notes:**

1. Anagrams are words that have same length and same frequency of characters but only the order is different.
2. If two words are anagrams, then if we sort them - they will end up as exactly same strings. Sorting each word efficiently has a time complexity of O(nlogn). If we sort each word in a list of size m, the time complexity will O(m.nlogn).
3. In order to better the time complexity, we move towards the more efficient solution. Here the idea is to group the anagrams using a hashmap.
4. For the keys, we will create a "character count array" for each word. Since all the characters are lowercase (a-z), an array can record the counts of the charachters from 0 - 25 (26 letters) where index 0 represents 'a' and 25 represents 'z'. This array of 26 character counts is set as a key. Pro TIP: Arrays cannot be set as dictiionary key. Convert this array to tuple so it can be set as a key. Pro Tip: take difference of ASCII values to calculate the correct index in the character count array. For example: if 'a' = 80 , 'b' =81 than to map it on zero and one index. 80-80=0, 81-80=1
   `ord(c)-ord('a')`
5. For values, we will append word/string whose count is calculated for character count array.
6. For our result hashmap use defaultdict and set it to list. Default dictionaries has a default key value. So it never thows key error.
7. Return only the values of the resultant hashmap.
