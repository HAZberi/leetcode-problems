class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        self.stack = []

        for c in tokens:
            if c == "+":
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif c == "-":
                self.a, self.b = self.stack.pop(), self.stack.pop()
                self.stack.append(self.b - self.a)
            elif c == "*":
                self.stack.append(self.stack.pop() * self.stack.pop())
            elif c == "/":
                self.a, self.b = self.stack.pop(), self.stack.pop()
                self.stack.append(int(self.b / self.a))
            else:
                self.stack.append(int(c))
        
        return self.stack[0]
            

#Test Cases

mySolution = Solution()

print("Test Case 1: " , mySolution.evalRPN(["2","1","+","3","*"]))
print("Test Case 2: " , mySolution.evalRPN(["4","13","5","/","+"]))
print("Test Case 3: " , mySolution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))