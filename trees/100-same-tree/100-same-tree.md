**Notes:**

1. The problem asks us to chech whether the two given trees are same. They should be similar in the structure and the nodes has the same values.
2. The problem idetifies itself as depth first search. We traverse to left most nodes then compare them then travese to right nodes compare them and then compound the result and return it.
3. The important thing here is to identify base cases. Following are the possiblies when we are comparing two nodes. Rest of the code is just traversing and compounding.
   1. if both roots are null. We return True
   2. If either of the root is null. We return False
   3. if we have both root values are not equal. We also return False. Pro Tip: We dont need to explicitly return Ture if both the root values are equal. We only need to catch when our comparision is false one time and only one time when the comparision is true. Our result will compound and pop up as True only if and if we encounter a False.
4. We make the recursive calls on the left subtrees and right subtrees. If we take the AND of lefts and rights result and return it.
