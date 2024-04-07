**Notes:**

1. Anagrams are exactly same in terms of length and frequency of similar characters. The only difference is the order of characters. Example: anagram and nagaram are Anagrams but car and rat are not.
2. First solution requires to copy all the characters of the strings with their frequencies in a hasmap. This will give us two hashmaps. Then iterate through one hashmap and compare the keys and values.
3. The time and space complexity for both is O(s + t).
4. Pro Tip: If a key doesnot exist in the hashmap. We can use the get method on the hashmap which can return a default value if the value doesnot exist. `myhashmap.get(otherhashmap[s[i]], 0)` like so.
5. Since its an easy problem, interviewer may ask to improve the space of complexity of this solution.
6. To improve the space complexity, we can sort both strings and simply return the comparision. In that case, space complexity with be O(1) "supposedly" because we are not sure if the sorting really doesnot use extra space. The time complexity of an efficient sorting algorithm is 0(nlogn).
7. If interview asks for the second solution just type this code out using python sorted function.  `return sorted(s) == sorted(t)`
