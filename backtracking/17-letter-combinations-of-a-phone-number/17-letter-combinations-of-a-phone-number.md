**Notes:**

1. The problem asks to find all the combinations of given string of digits, where each digit is mapped to 3 or 4 alphabets as it was mapped on older phones.
2. Since we are required to find to all the combinations, so we have to use the bruteforce approach, in other words backtracking. The solution we are looking to devise is O(n . 4 ^ n). where n is the number of digits and 4 is the maximum number of alphabets mapped to a digit.
3. The first thing right of the bat, is to create a dictionay to map each digit to its corresponding string of alphabets. We will also have a resultant list that wil store all the combinations.
4. The idea is to create a decision tree, for each digit we have three or four different alphabets and then in the second level we can pick the second digit and each alphabet in the first level now has three or four different alphabets to concatenate with. So in our backtrack function we basically need to go over all the alphabets of the current digit in a loop and then make the recursive call for the next digit and concatenate the current alphabet to the current string. As our base case, whenever length of current string becomes equal to the length of digits we append the current string to the resultant list.
5. We will define the backtrack function with i as iterator for the digits, a current string which will hold the current string. This current string will be added to the resultant list.
6. Our base case is whenever length of the current string becomes equal to the length of digits, we append the current string to the result and return.
7. Then we loop over all the letters that are assoicated with the digit key in our dictionary. And for each letter we make the recursive call, with iterator set to next digit (i + 1) and also updating the current string by concatenating it with the current letter.
8. Outside our recursive function we have to do a small check, to meet the requirements of the output. We only call the backtracking function if the length of digits is not zero. Then we simply return the resultant list.