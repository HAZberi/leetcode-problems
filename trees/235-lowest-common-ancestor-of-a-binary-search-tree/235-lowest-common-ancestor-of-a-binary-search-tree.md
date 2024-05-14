**Notes:**

1. This problem is basically asking us to find common parent of two given nodes in a tree. The root is a common parent of all the nodes in the tree. But the problem is asking to find the lowest common parent or ancestor.
2. Our given tree is a binary search tree BST, it means in order to be an immediate parent of both nodes. One of the node's value should be smaller than the parent and the other node's value should be greater than the parent node's value. As soon as we hit this case we simply return the parent.
3. There is one more case, if one of the node's value is equal to the parent/curr node. In that case we will also return this parent/curr node.
4. So basically if both the node values is greater than the current or parent node value. We move to the right of the tree. By setting our current to right of current. If both the node values is smaller than the current of parent node value then we move to the left of the tree. By setting our current to left of current.
5. In all other conditions, we have reached the lowest common anscestor, we will simply return current/parent.
6. Since we are going through each level and hit only one node at each level. The time complexity of this algortihm is O(logn) and space is constant O(1)
