class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bottom = ROWS - 1

        while (top <= bottom):
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break
        
        if (top > bottom):
            return False 

        L, R = 0, COLS - 1
        row = (top + bottom) // 2
        while (L <= R):
            mid = (L + R) // 2

            if matrix[row][mid] < target:
                L = mid + 1
            elif matrix[row][mid] > target:
                R = mid - 1
            else:
                return True
        return False

#Test Cases:

mySolution = Solution()
print("Test Case 1: ", mySolution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print("Test Case 2: ", mySolution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))