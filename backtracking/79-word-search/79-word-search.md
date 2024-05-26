**Notes:**

1. The problem asks us to find whether a given target word is in the board such that each character of the word is vertically or horizontally adjacent to the next character.
2. There are no shortcuts to find the solution to this problem. We have to check each and every cell of the board whether the character matches the first character of the board. If yes, then we will check whether the next character in the word is adjacent to it. If not, we will check the next position on the board.
3. We will have to use backtracking to recursively find the path of the word as soon as we find the first match.
4. First we need to take the bounds of the board. Rows is equal to length of input board. Columns is equal to length of the first row in the board.
5. Then we need to keep track of the path at which we have already found the matching character. We also need to make sure that we dont visit any cells on this path again when ever looking for adjacent cells. So we will keep a hashset for path and store all the positions that matches with the word.
6. After that we define the backtrack function which will take the position (row, col) of the board as an argument and also an i iterator which iterates over the word, move to next character, whenever we are making any recursive calls.
7. First whenever our i iterater is equal to the length of the word we will simply return true.
8. Second if we out of bounds from the board OR current character doesnot match the character at this position on the board OR the current cell exists in the path hashset (meaning we have already visited it and it was matching as well). We will simply return false.
9. After both of these edge cases, we have a matching character, so we add this position in our hashset.
10. The we make recursive calls on all of the four neighbours for the next character in the word. Left, right, up, down. If any one of the neighbours returns true, we will also return true or if none returns true then we simply return false.
11. Since we added the position in our hashset, we need to remove it from the hashset because we might not have found the path so, we need to clear that position after our recursive calls.
12. Outside our recursive function. We do a nested loop, since we have to check the neighbours of all the cells one by one. Inside the nested loop we check the result of our backtrack function. If our backtrack function returns true we return true. Otherwise, in the next iteration we start again from the first character.
13. Finally if the nested loop doesnot return true. We will return false, outside the nested loop meaning the target word is not present on the board.
14. The time complexity of this problem is O(n x m x 4w) where m is the rows in the board, n is the cols in the borad and w is the length of the word and 4 because we are making for recursive calls at each cell.
