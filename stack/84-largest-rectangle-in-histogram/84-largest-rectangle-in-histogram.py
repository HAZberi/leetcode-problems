class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = [] # pair[index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

#Test Cases

mySolution = Solution()
print("Test Case 1: ", mySolution.largestRectangleArea([2,1,5,6,2,3]))
print("Test Case 1: ", mySolution.largestRectangleArea([2,4]))