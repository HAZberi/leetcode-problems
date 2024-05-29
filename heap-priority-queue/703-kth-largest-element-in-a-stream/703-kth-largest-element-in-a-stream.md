**Notes:**

1. The problem asks us to design a kth largest data structure such that whenever we add a value to the structure, it returns the kth largest element. The structure is initialized by a list of intergers.
2. The first solution is to sort the list and that will get access to the kth largest element. But then we want to add a value to this list. We can find out the exact position to insert in O(logn) time using binary search but inserting in a list is O(n) time operation.
3. Can we use a data structure that can add the new element in O(logn) time and get us the kth largest in O(1). Yes we can use a min heap of size k. The reason we are using the minHeap, because we keep the size of min heap equal to k. Whenever we add a value to heap and the length of heap goes over the size k. Then we pop a value from Heap. This way we will always have access to the kth largest element at the root of the heap.
4. First we have to initialize our minHaep, we will add all the elements from the given to the minHeap by calling the python built in heapify method. Then we will run a loop and keep poping off values from the heap until we the length of heap is equal to k.
5. Then in our add method, we will add the incoming value to our heap first. Then check whether the length of heap is greater then k, if it is, then we pop off from the heap. Finally we return 0 index of the heap. This will have the kth largest element.
6. Constructor is O(n.logn) while the add method is O(logn)
