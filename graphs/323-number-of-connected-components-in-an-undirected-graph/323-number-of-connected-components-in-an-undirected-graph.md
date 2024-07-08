**Notes:**

1. The problems ask to find the total number of components in an undirected graph. Since a graph can be disconnected, so we have to find how many contigous sets of nodes are actually present in a graph.
2. A simple or more brute force approach of solving this question is to use the recursive DFS method. We have to run DFS and add processed nodes in the visited hashset. If we encounter a node that is already been visited, it means its part of the same component. If we encounter a node that has not been visited, it means its part of a different component.
3. Lets discuss a genric algorithm to solve this problem step by step.
   1. Make an adjacency list by using the given information.
   2. Initialize a visited hashset. This will store all the nodes that has been visited. We also initialize numComponents variable to 0. This will be our final result.
   3. Define the recursive DFS method and supply it with a node for traversal. Start by checking all the neighbours of the current node by looping over the list. Inside the loop, check if the neighbour has not been visited yet, add this neighbour to the visited hashset and recursively call the DFS on this neighbour. We dont have to return anything from this method. We are just adding the non-visited nodes to the visited hashset.
   4. Outside the DFS method. We loop over all the nodes and check if the current node has been visited. If a node is not visited then we first add it to the visited hashset and then run our recursive DFS method on this node. After that we also increment the numComponents by 1.
   5. Finally we return the numComponents.
5.
