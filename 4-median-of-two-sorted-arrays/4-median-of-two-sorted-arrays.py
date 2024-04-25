from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B): #A should be the smaller array
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            midA = (l + r) // 2
            midB = half - midA - 2 #Correct index of midpoint

            ALeft = A[midA] if midA >= 0 else float("-inf")
            BLeft = B[midB] if midB >= 0 else float("-inf")
            ARight = A[midA + 1] if (midA + 1) < len(A) else float("inf")
            BRight = B[midB + 1] if (midB + 1) < len(B) else float("inf")

            if ALeft <= BRight and BLeft <= ARight: #correct partition 
                if total % 2: #If we have odd number of elements
                    return min(ARight, BRight)
                else: 
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = midA - 1
            else:
                l = midA + 1


#Test Cases

mySolution = Solution()

print("Test Case 1:", mySolution.findMedianSortedArrays([1,3], [2]))
print("Test Case 2:", mySolution.findMedianSortedArrays([1,2], [3,4]))
print("Test Case 3:", mySolution.findMedianSortedArrays([1,2,3,4,5,6,7,8], [1,2,3,4]))
