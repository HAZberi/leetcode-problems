**Notes:** 

1. The problem asks us to find all the possible subset of a given list. The list may contain duplicates but we have to generate unique subsets.
2. This problem is very similar to the first subset problem. The only problem is to remove the duplicates sets. The only way to know about the duplicates is to sort the given list. Then all the duplicates will be next to each other and then we will be able to skip the duplicates.
3. Our decision tree in this case will be as follows. First we will add the current value to the current subset and then we will not add the value to current subset. The important thing to note here, when we are not adding the current the value to the current subset, then we must skip all the duplicate values of the current value as well. So in the next iteration when we add the next value, it will be after the current value and all its duplicates.
4. We will intialize a result list to store all the subsets.
5. Then we define our recursive backtrack function, which will take the index i as the iterator for the given list in our recursive calls. We will also pass the current subset.
6. Our base case is whenever we reach the end of the given list. At that point we wiil simply append the copy of current subset to our resultant list.
7. After that we have two choice to make, One to include the current element in the subset, we will simply append the current element to the current subset. Then we will call the recursive function with an increment to the i iterator.
8. Then we will have to make our second choice, which is not to include the current element. So we pop for the current subset. Then we will have to run a loop untill our iterator goes out of bounds and current element is equal to the next element, we will keep incrementing our iterator. After that we simply call our recursive function with an increment to the i iterator.
9. Outside the recursive fucntion we will simply call the backtracking function with initial i=0 and current subset = []. and return the function call.
