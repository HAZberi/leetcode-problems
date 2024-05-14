**Notes:** 

1. Polish reverse notation is a way of doing arithmetic operations. These operation can be done via stack data structure.
2. First we have to read the array from left to right in a for loop. Each integer value is placed on to the stack until we encounter a "+", "-", "*" and "/".
3. Whenever we hit a "+" and "*". We pop two elements from the stack, do the operation and append the result back to the stack.
4. Whenever we hit a "-" and "/". We also pop two elements from the stack. But here the order of the numbers is important. The first value popped should be subtracted from the popped second value. So we have to store the both the values. Then do the operation on stored values and then append the result back to the stack.
5. The division should always round towards zero. By default python uses decimal division. So to counter that we should just simply convert the division result to integer, which will automatically round it towards zero.
6. If we encounter any other characters other than the operations itself. Those are basically integers. So we convert those characters into an integer and just simple add it on to stack.
7. At last, there will be only one value on the stack when we finish looping the input list. Retrun the value at the 0th index of the stack.
8. The Time complexity of this solution is O(n). Since go over the array one time and pop values out of the stack one time. The space complexity is also O(n) since we are using a stack.
