from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            #processing top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #preocessing right column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #processing the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            #processing the left row 
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

#Test Case
mysolution = Solution()
print("Test Case 1: ", mysolution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print("Test Case 2: ", mysolution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

