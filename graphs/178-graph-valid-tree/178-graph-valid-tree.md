**Notes:**

1. The problem asks us to find whether a given set of graph is a valid tree. The graph is given in the form of number of total vertices and a list of edges. It is mentioned that the graph is undirected and also that all the edges are unique.
2. This problem can be solved by both DFS and BFS but here we will be solving this problem with the DFS approach.
3. The primary clarification question that can be asked or disscussed here is that what is a valid tree or whats the difference between a graph and a tree.

   1. A graph can have loops, trees on the other hand do not have any loops.
   2. A graph can be disconnected but trees cannot be disconnected.

   It should be made clear that these only these two conditions make a graph a valid tree.
4. The first task is to create an adjacency list from the given information. Use a hashmap by initializing it as key=>vertex, and the value of each vertex is an empty list. Then loop through the list of edges and populate all the neighbours of each vertex. Note that you have to append node1 and node2 as neighbours of each other.
5. Before even writing the DFS method, we should know that we need a hashset to detect any cycles in the graph. So we initialize a visited hashset. As soon we visit a vertex, we add it to the hashset before moving forward.
6. There is one more important thing to consider while writing the recursive DFS method. Since the graph is undirected, whenever we make a recursive call, the previous node will be the neigbour of current node. So we have to make sure the we should skip the previous node when making recursive calls on the neighbours of the current node. So our DFS method will be supplied with a current node and a previous node.
7. In the DFS method first we check whether the current node exists in the visited hashset. If it is, then simply return False. Otherwise we will simply add it to the visited set. Then we run the recursive dfs on all of the neighbours of this current node in a loop. If we encounter a previous node as a neighbour we will simply skip the current iteration. Otherwise we make the recursive call on the neighbours and if the recursive call returns a False, we will immidiately return False. If we break out of the neighbours loop, we will simply return True.
8. Finally before calling the recursive DFS we should keep in mind the 2 conditions of a valid tree. First they should be no cycle, which we can detect by simply calling the DFS method. Second we need to make sure that its connected, which we can convieniently do by simply checking if the total number of vertices is equal to the len of the visited hashset. We return AND of these two conditions.
9. There is one edge case that we missed earlier, that if there is no vertex or the total number of verticies is zero.
