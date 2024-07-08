**Notes:**

1. The problems ask to find the total number of components in an undirected graph. Since a graph can be disconnected, so we have to find how many contigous sets of nodes are actually present in a graph.
2. A simple or more brute force approach of solving this question is to use the recursive DFS method. We have to run DFS and add processed nodes in the visited hashset. If we encounter a node that is already been visited, it means its part of the same component. If we encounter a node that has not been visited, it means its part of a different component.
3. Lets discuss a genric algorithm to solve this problem step by step.

   1. Make an adjacency list by using the given information.
   2. Initialize a visited hashset. This will store all the nodes that has been visited. We also initialize numComponents variable to 0. This will be our final result.
   3. Define the recursive DFS method and supply it with a node for traversal. Start by checking all the neighbours of the current node by looping over the list. Inside the loop, check if the neighbour has not been visited yet, add this neighbour to the visited hashset and recursively call the DFS on this neighbour. We dont have to return anything from this method. We are just adding the non-visited nodes to the visited hashset.
   4. Outside the DFS method. We loop over all the nodes and check if the current node has been visited. If a node is not visited then we first add it to the visited hashset and then run our recursive DFS method on this node. After that we also increment the numComponents by 1.
   5. Finally we return the numComponents.
4. The second and more optimal solution to this problem is using the algorithm of union find. Basically we start from all the nodes disjointed, meaning each node is itself a parent. Then we go the edges and try combine two nodes at a time. If we successfully combine the two nodes then we decrement 1 from the total number of nodes. But before we join the two nodes, we need to know two things:

   1. Root Parent of both nodes
   2. Rank/Size of the Root Parents

   In order to find the root parent of the node, we will define a find method.
5. The find method can be written iteratively or recursively (check python playground for implementation and neetcode union find design question video). Basically in the iterrative method, the loop termination condtion is once we find the root. The root has found if the result value is equal to the parent of result value. Inside the loop we do things:

   1. Path compression by setting the parent of the current node to its parent. That way we are moving up the tree by two steps.
   2. Then set the grandfather to result value.

   Outside the loop we simply return the result value.
6. In the union method, first we check whether root parents of both the nodes are equal. If they are equal then we simply return 0. This also means that there is a cycle and also that both of these nodes are part of the same component. After that we check the rank/size of root parents, we assign the larger root parent as the root parent of smaller root parent. Also we add the rank of smaller root parent to the rank of larger root parent. ProTip: Use if else condition to assign root parents and increment ranks. Once the union is successful then retrun 1.
7. Outside the union and find methods, loop over the edges and decrement the total number of nodes if the call to union function on both of the nodes returns 1. If the union function return 0 then there will be no decrement in the number of nodes. Finally simply return the number of nodes. ProTip: assign are res variable to n. And then keep on decrementing res, and finally return res instead.
