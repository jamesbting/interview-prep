Successor and Predecessor
Successor = "after node", i.e. the next node in the inorder traversal, or the smallest node after the current one.

Predecessor = "before node", i.e. the previous node in the inorder traversal, or the largest node before the current one.

img




Approach 1: Iteration
Intuition

There are two possible situations here :

Node has a right child, and hence its successor is somewhere lower in the tree. To find the successor, go to the right once and then as many times to the left as you could.
pic

Node has no right child, then its successor is somewhere upper in the tree. To find the successor, go up to the node that is left child of its parent. The answer is the parent. Beware that there could be no successor (= null successor) in such a situation.
pac

fic

Algorithm

If the node has a right child, and its successor is somewhere lower in the tree. Go to the right once and then as many times to the left as you can. Return the node you end up with.

Node has no right child, and hence its successor is somewhere upper in the tree. Go up till the node that is left child of its parent. The answer is the parent.

Implementation


Complexity Analysis

Time complexity: O(H), where H is the height of the tree. That means O(logN) in the average case, and O(N) in the worst case, where N is the number of nodes in the tree.
Space complexity: O(1), since no additional space is allocated during the calculation.