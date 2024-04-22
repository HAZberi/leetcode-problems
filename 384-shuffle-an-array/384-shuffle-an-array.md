**Notes:**

1. This is a very simple problem. We will use standard python library to generate random indices and copy lists using list function.
2. The problem asks us to reset and shuffle a list of unique elements.
3. In the constructor, initialize the nums list and also a true copy of nums list stored as orginal list.
4. In the reset method. Make a true copy of orginal list and set it as nums list. Then simply returned the list.
5. In the shuffle method, we will the use the popular method of shuffling algorithm known as Fisher Yates Algorithm. In Fisher Yates Algorithm we use a backward loop (starting the loop from the end of the array). For each index i we calculate a random integer index for the rest of the array `randint(0, i)`. Then we swap the element at random index with element at current index.
6. The Backword loop makes sense because when we do the permutaions of combinations. The natural flow is always 5 x 4 x 3 x 2 x 1.
7. ProTip: We dont have to iterate all the way upto index 0. We can terminate the loop at index 1 because the last unshuffled element will always stay at the same index, since rest of all the list is already shuffled.
