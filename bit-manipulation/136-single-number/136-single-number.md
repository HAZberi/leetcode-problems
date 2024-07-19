**Notes:** 

1. The problem asks us to find the single number in an array, where there is a unique number and rest of the numbers have duplicates (only twice) in the list. So basically we have to find that unique number.
2. This problem can be solved by a hashset, where we keep on adding the new unique numbers to the hashset and whenever we have a duplicate we remove it from the hashset. So all in all we will only be left with the unique number. Though its a valid solution but the problem asks us to specifcally find the solution in O(1) space. So this is not a valid approah.
3. The intituion to solve this problem in constant space is use XOR operation. If we simply take the XOR of all the elements in the list, we will be left with the unique number because duplicates cancels out.
4. If we refer to the truth table of the XOR. We know that 0,0 is 0 and 1,1 is also 0, while 1,0 and 0,1 is 1. So all the duplicates will cancel out each other and we will be left with the only unique number.
