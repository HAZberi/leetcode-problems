from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            for i in range(r - l): #(n - 1) rotations
                top, bottom = l, r

                #store top left
                topLeft = matrix[top][l + i]

                #replace top left with bottom left
                matrix[top][l + i] = matrix[bottom - i][l]

                #replace bottom left with bottom right
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #replace bottom right with top right
                matrix[bottom][r - i] = matrix[top + i][r]

                #replace top right with stored top left
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1

#Test Case 
mysolution = Solution()
test_case_1 = [[1,2,3],[4,5,6],[7,8,9]]
test_case_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
mysolution.rotate(test_case_1)
mysolution.rotate(test_case_2)
print("Test Case 1: ", test_case_1)
print("Test Case 2: ", test_case_2)

