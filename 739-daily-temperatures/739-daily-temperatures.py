class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] #pairs [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndx = stack.pop() #destructuring
                res[stackIndx] = i - stackIndx
            stack.append([t, i])
        
        return res
    
#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.dailyTemperatures([73,74,75,71,69,72,76,73]))
print("Test Case 1: ", mySolution.dailyTemperatures([30,40,50,60]))
print("Test Case 1: ", mySolution.dailyTemperatures([30,60,90]))