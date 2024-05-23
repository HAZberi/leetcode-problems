**Notes:** 

1. The problem asks us to generate all the possible subsets of the given list of numbers. All the numbers in this list are unique.
2. This is a backtracking problem because we have to generate all the subsets and not the number of subsets. So in this case we will use recusive dfs for the decision tree. Our decision tree will have to branches, one to include the current element in the subset and the second one to not include the element in the subset. So we will make recursive calls after each decision.
3. Before the definition of our recursive function we will initiate two empty list. One list will hold all the resultant subsets and the second list will hold the current subset.
4. Then we define our recursive function and it will be provided the index argument. This index "i" will be the iterator for our recursive calls to move to the next element in the numbers list.
5. Our base case is whenever i is greater than equal to the length of numbers list, meaning we have processed all the numbers and have made decisions on all of the elements. We append the copy of current subset to our resultant array. Then simply return.
6. Then we take our first decision, to include the current number in the subset list. We append the current number at ith index in the subset list. The we  make the recursive call with now i = i+1.
7. Then we take our second decision, now we pop this element from the subset list that we just added. Then we simply call the backtracking method again with i = i + 1.
8. Outside our recursive function we will simply call the recursive function which will populate the resultant list. Then we simply return the resultant list.
