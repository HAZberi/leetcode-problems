**Notes:**

1. In this problem we have to make sure that every open parenthesis has the same closing parenthesis and the order should also be correct.
2. When we are reading from the input string character by character, how do we know we have the closing parenthesis or the open parenthesis?. To solve this issue we can create a closed-to-open parenthesis dictionary/hashmap. But what should be the keys of this hashmap, opened or closed parenthesis?
3. Whenever we encounter the open parenthesis we have to keep on checking the next character until we encounter a closing parenthesis. But as soon we encounter the closing parenthesis, we have to decide and check whether we have completed the set of brackets, and always the last checked bracket should be the same opening one. This type of situation clearly identifies that we should use a **stack,** since we always have to decide based on the last checked value.
4. So back to our question, what should be the keys of the hashmap. Since we always have to decide and check at the closing paranthesis, the keys of the hashmap is the closing parathesis and values are the corresponding open parenthesis.
5. If we encounter open parathesis we just append it to the stack.
6. if we encounter close parathesis we check it in our hashmap and also peek the stack (basically check last value in the stack `[-1]`) . If the last value is equal to the value of the closing parenthesis in our hashmap. We pop out the last element. Otherwise we will simply return false.
7. At the end we just need to check whether the stack is empty or not, if there are no values in stack we return true, otherwise false.
