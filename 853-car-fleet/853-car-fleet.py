class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        stack = [] #For Time to Targets

        for i in range(len(cars) - 1, -1, -1):
            p , s = cars[i]
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

#Test Cases

mySolution = Solution()

print("Test Case 1: ", mySolution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print("Test Case 2: ", mySolution.carFleet(10, [3], [3]))
print("Test Case 3: ", mySolution.carFleet(10, [0,2,4], [4,2,1]))