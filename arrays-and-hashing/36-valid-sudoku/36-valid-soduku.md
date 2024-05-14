**Notes:**

1. The program requires us to find a valid sudoku board. The 3 rules are given, all rows, all columns should be unique. And the 3x3 squres should be uinque as well.
2. Since the program clearly requires us to check the unique values we can make use of HashSet.
3. For rows and columns we can use a dictionary where indices can be keys and values can use the HashSet data structure.
4. For 3x3 square, a good strategy is to group the indices as such `0:012, 1:345, 2:678` So the entire 9X9 sudoku board is converted into a 3x3 with 0,1,2 indices for columns and rows. Like rows and columns we will use a Hashmap where values use the HashSet data structure. For keys, we divide (integer divide) the actual row/col number with 3 to obtain a row and col in the range of 0,1,2.
5. The time complexity for this problem is O(9^2). Since we have to traverse the entire board.
6. We should ignore the empty values ".", and continue the loop to next iteration.
7. We perform an elaborated check before putting values in the dictionaries. If our check identifies a duplication, we can just return False.
