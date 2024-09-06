from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowFirst = False
        ROWS, COLS = len(matrix), len(matrix[0])

        #determine which rows and cols need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowFirst = True
        
        #Zero flagged rows and columns except the first row and column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        #Zero first column
        if matrix[0][0] == 0:
            for r in range(1, ROWS):
                matrix[r][0] = 0

        #Zero first row
        if rowFirst:
            for c in range(COLS):
                matrix[0][c] = 0 

#Test Case
mysolution = Solution()
test_case_1 = [[1,1,1],[1,0,1],[1,1,1]]
test_case_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("Test Case 1: ", mysolution.setZeroes(test_case_1), test_case_1)
print("Test Case 2: ", mysolution.setZeroes(test_case_2), test_case_2)

