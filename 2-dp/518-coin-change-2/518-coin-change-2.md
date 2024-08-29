**Notes:**

1. The problem asks us to find the total number of valid combination that make up to the target amount.
2. We are given a list of coins and a target amount. How many ways we can return the change? What would be the brute force appraoch of solving this problem. This problem can be solved the 0/1 unbounded knapsack algorithm. So the basic idea is to draw the recursive tree for the problem using every coin and the remaining amount. Ou recursive tree will start from the amount 0. Then we can either include the first coin or skip the first coin. If we include the first coin, then the new amount will be the difference of
