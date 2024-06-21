**Notes:**

1. The problem asks us to make a deep copy of a given graph node. A graph node has a value property and a second property of neighbours list.
2. Like all graph problems we have to traverse the nodes of the graph and the ones we have visited or processed, we put those in a hashmap. So in this problem we will use a hashmap, right of the bat.
3. This problem can be solved with both dfs and bfs. The dfs will be more straightfoward. The intution for dfs is that, we make a copy of current node with just the value, but at this point we haven't make the copy of the neighbours, we dont even know if the neighbours even exist. So we run the dfs on each of the neighbours. We recursively make copies of the neighbours and add it to the current nodes neightbours list.
4. So we will have three steps of cloning the graph using a hashmap.
   1. Our base case for the recursive dfs is to check if we have already proceesed (made a copy) of current node. So we simply check in our hashmap. If the new node exists at the key of old node. We will simply return the new copy node.
   2. Second step is the process of cloning. After the base case, we will make the copy of current node with the value only and immediately added it to our hashmap. That way we will know that we have already made a copy of this node.
   3. In order to make the complete copy of this node, we have to copy all the neighbours. Since we have to make the copy we will make our recursivec call on each neighbour of the current old node to make the true copy of the neighbours and append the copy to current copy node's neighbours list.
5. Once we have deep copied all the neighbours of the current copy node, we will simply return the copy node.
6. Outside of our dfs function we will simply call this recursive dfs function with given graph node and return it if the given graph node is not null otherwise we will simply return None.

"""

# Definition for a Node.

class Node:

    def__init__(self, val = 0, neighbors = None):

    self.val = val

    self.neighbors = neighbors if neighbors is not None else []

"""

from typing import Optional

classSolution:

defcloneGraph(self, node: Optional['Node']) -> Optional['Node']:
