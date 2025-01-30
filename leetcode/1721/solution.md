Solution
Overview

This is a simple problem based on the Linked List data structure. If you have solved problems using a Linked List before and have a basic idea on how a Linked List is traversed and modified, this problem will be easy to implement.

The general idea behind the problem is that we have to find the kth node from the beginning and the kth node from the end of the Linked List. Once we have pointers to both of these nodes, we could simply swap their values.

    The problem description states that we have to swap the values of the nodes. Therefore, the actual nodes in the Linked List should remain unchanged and there is no need to change the actual list node pointers.

In this article, we're going to look at 3 different approaches. Each approach further reduces the number of passes we need to do through the list. Let's look at the approaches in detail.
Approach 1: Three Pass Approach

Intuition

Given the problem to swap 2 nodes in the linked list at kth position, we need to position 2 pointers. The first pointer would point to the kth node at the beginning of the list given by frontNode. The second pointer would point to the kth node at the end of the list given by endNode.

Finding the position of frontNode is simple. We can start traversing from the head node until we reach the kth node. But to find the endNode, we must first know the length of the Linked List. If the length of the Linked List is listLength, the kth node from the end would be the (listLength - k)th node.

The following figure illustrates the idea.

img

Algorithm

As explained above, we must implement the algorithm using 3 separate passes.

Pass 1: Find the length of the Linked List by traversing each node in the list from head node to last node and increment the counter by 1. Let the counter used to find length be listLength.

Pass 2: Traverse until the kth node from the head node and set the frontNode.

Pass 3: Traverse until the listLength - k node from the head node and set the endNode.

    Swap the values of frontNode and endNode using temporary variable temp.

    Return the head node.

Implementation

Complexity Analysis

    Time Complexity : O(n), where n is the length of the Linked List. We are iterating over the Linked List thrice.

    In the first pass, we are finding the length of the Linked List which would take O(n) time.

    In second pass and third pass, we are iterating k and n - k times respectively. This would take O(k+n−k) i.e O(n) time.

    Thus, the total time complexity would be O(n)+O(n)=O(n).

    Space Complexity: O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode and currentNode.

Approach 2: Two Pass Approach

Approach 1 solved the problem with three passes, in O(n) time. We can't do better than O(n), because all valid solutions must count how many nodes there are in order to be able to find the kth last node. But while we know we can't do better than O(n), it's still often preferable to minimize the number of loops needed for Linked List problems.

    Interview Tip: Reducing the number of passes/separate loops is a very common follow-up question for Linked List problems.

The first optimization we could think of over the three pass approach is that we could find the length of the Linked List as well as the position of frontNode in a single pass.

To find the length of the Linked List we are iterating from the head node until the end of the Linked List. On the way, we would also come across the kth node from the head of the list and we could set the frontNode pointer at the point.

Algorithm

The problem can be solved in two passes with the following steps:

    Iterate from the head of the Linked List until the end and store the length found in listLength. In the same loop, check if we have reached the kth node, and if so, set frontNode to point at that node.

    Iterate from head node until listLength - k node and set the endNode.

    Swap the values of frontNode and endNode using temporary variable temp.

    Return the head node.

Implementation

Complexity Analysis

    Time Complexity : O(n), where n is the length of the Linked List. We are iterating over the Linked List twice.

    In the first pass, we are finding the length of the Linked List and setting the frontNode which would take O(n) time.

    In the second pass, we are setting the endNode by iterating n - k times.

    Thus, the total time complexity would be O(n)+O(n−k) which is equivalent to O(n).

    Space Complexity: O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode and currentNode.

Approach 3: Single Pass Approach

Intuition

Can we implement the problem in a single pass?
The problem is that to find the position of endNode we must know the length of the Linked List. And to find the length of the Linked List we must have iterated over the list before at least once.

However, we could use a trick to find the position of the pointer endNode in a single pass. The trick is:

If endNode is k positions behind a certain node currentNode, when currentNode reaches the end of linked list i.e at nth node , the endNode would be at the n−kth node.

    A similar trick is used in a few other Linked List problems like Remove Nth Node From the End of List and the Fast and Slow Pointer Approach in Find The Middle Of Linked List.

The following figure illustrates the idea.

img

Let's see how we can implement this approach.

Algorithm

The problem can be implemented in a single pass using the following steps,

    Start iterating from the head of the Linked List until the end using a pointer currentNode.

    Keep track of the number of nodes traversed so far using the variable listLength. The listLength is incremented by 1 as each node is traversed.

    If listLength is equal to k, we know that currentNode is pointing to the kth node from the beginning. Set frontNode to point to the kth node. Also, at this point, initialize endNode to point at the head of the linked list. Now we know that endNode is k nodes behind the head node.

    If endNode is not null, we know that it is positioned k nodes behind the currentNode and so we increment endNode in addition to currentNode. When currentNode reaches the end of the list, endNode would be pointing at a node which is k nodes behind the last node.

    Swap the values of frontNode and endNode using temporary variable temp.

    Return the head node.

Implementation

Complexity Analysis

    Time Complexity : O(n), where n is the size of Linked List. We are iterating over the entire Linked List once.

    Space Complexity: O(1), as we are using constant extra space to maintain list node pointers frontNode, endNode and currentNode.
