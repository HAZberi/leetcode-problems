**Notes:** 

1. The problem asks us to find all the possible permutations of given list. We have to return a list of lists containing all the possible permuations.
2. This problem has many solution. We know two backtracking solutions. One of the solutions is included in the python playground where we have done it with both recursion and itration. However, here we will be solving the same problem with a slightly different approach.
3. We will initiate a resultant list that will contain all the permutations.
4. In this solution we will also use recursion, we will keep popping off the first value from the given list and then make the recursive call with the updated list. This step will be done in a loop where iterator i starts at zero and runs till the end of the given list. It is important to remember here that all the values that we pop off will be added to the end of the given list at the end of the loop.
5. Our base case is whenever we are left with just 1 value in the list. One value on its own has only one permutation. So this will be our base. In this case we will have to return a list of lists by copying the current given list in a list like so.`[nums.copy()]`or the more efficient python way of copying ` [nums[:]]`
6. Our recursive call will return a list of permutations. Now we have to add the popped element at the end of each permutation. This will be done in a loop becuase we will be having multiple permutations for the last element popped.
7. After that we wiil add all these permutations in our result. Instead of using a loop again, we can use a python way of adding multiple values to a list like so. `list.extend(list_items)`
8. Our final step before exiting the outer loop is to add the popped element back to the given list but at the end of the list. We will keep on doing that and at last our given list is exactly the same as where we started the problem. Outside the outer loop we will simply return the resultant list.
