**Notes:**

1. The first thing to notice in this problem is to truly understand the valid combination of parentheses. A valid combination must have equal number of open and closing parentheses.
2. The next most important thing to notice is the order of parentesis. A combination cannot start with a closed parenthesis. It has to an open parenthese. If there is an open parentheses only then we can add the closing parentheses.
3. This problem can be solved by backtracking. Because we dont know how many possible and valid combination we can generate.
4. The base case for valid parentheses combination is complete when number of open and closed brackets is equal to n. At this point we can take all the values from our stack, join them is a string, and append it to the resultant array. If we use a string instead of stack we append the string to the resultant array at this point. Join iterables in python like so `"".join(iterable)`
5. If the open parentheses count is less than "n". We add one open parantheses to the stack. Then we call the backtracking function again and increment the open parentheses count by 1. Once the bactracking is done we pop out the value we added to the stack.
6. if the close parentheses count is less than the open parentheses count. We add a close parentheses to the stack. Then we call the backtracking function again and increment the close parentheses count by 1. Once the backtraking is done we pop out the value we added to the stack.
7. By the end of this backtracking. We call the backtracking function with 0 open parentheses count and 0 closed parentheses count.
8. Then just simply return the resultant array.
