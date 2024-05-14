**Notes:**

1. In this problem we have ot implement basic features of a stack like push, pop, get and one advance feature which is getting the minimum value.
2. In python we use, the normal list. It exactly behaves like a regular stack. We only need to think about getting the minimum value of stack.
3. One way is to go through the entire stack and maintain a min value. But this will be O(n). The problem indicates that getting the minimum value should be in constant time.
4. So, we have to use two stacks, first our normal stack, second a min stack, which stores the min value at each level of our normal stack. whenever we push a value to our stack we push the minimum value at that point in the min stack as well. That's how we will be able to maintain a min stack.
5. Pro Tip: Use a ternary operation to check whether min stack is empty or not. if empty than we will take the current value as the minimum value.
