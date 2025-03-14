Video Solution
 
Solution Article
Approach 1: Heap

Let's start from the simple heap approach with O(Nlogk) time complexity. To ensure that O(Nlogk) is always less than O(NlogN), the particular case k=N could be considered separately and solved in O(N) time.

Algorithm

    The first step is to build a hash map element -> its frequency. In Java, we use the data structure HashMap. Python provides a dictionary subclass Counter to initialize the hash map we need directly from the input array. This step takes O(N) time where N is a number of elements in the list.

    The second step is to build a heap of size k using N elements. To add the first k elements takes a linear time O(k) in the average case, and O(log1+log2+...+logk)=O(logk!)=O(klogk) in the worst case. It's equivalent to heapify implementation in Python. After the first k elements we start to push and pop at each step, N - k steps in total. The time complexity of heap push/pop is O(logk) and we do it N - k times which means O((N−k)logk) time complexity. Adding both parts up, we get O(Nlogk) time complexity for the second step.

    The third and last step is to convert the heap into an output array. That could be done in O(klogk) time.

In Python, library heapq provides a method nlargest, which combines the last two steps under the hood and has the same O(Nlogk) time complexity.

diff

Implementation

Complexity Analysis

    Time complexity : O(Nlogk) if k<N and O(N) in the particular case of N=k. That ensures time complexity to be better than O(NlogN).

    Space complexity : O(N+k) to store the hash map with not more N elements and a heap with k elements.


Approach 2: Quickselect (Hoare's selection algorithm)

Quickselect is a textbook algorithm typically used to solve the problems "find kth something": kth smallest, kth largest, kth most frequent, kth less frequent, etc. Like quicksort, quickselect was developed by Tony Hoare and is also known as Hoare's selection algorithm.

It has O(N) average time complexity and is widely used in practice. It is worth noting that its worst-case time complexity is O(N2), although the probability of this worst-case is negligible.

The approach is the same as for quicksort.

    One chooses a pivot and defines its position in a sorted array in a linear time using the so-called partition algorithm.

As an output, we have an array where the pivot is in its perfect position in the ascending sorted array, sorted by the frequency. All elements on the left of the pivot are less frequent than the pivot, and all elements on the right are more frequent or have the same frequency.

Hence the array is now split into two parts. If by chance our pivot element took N - kth final position, then k elements on the right are these top k frequent we're looking for. If not, we can choose one more pivot and place it in its perfect position.

diff

If that were a quicksort algorithm, one would have to process both parts of the array. That would result in O(NlogN) time complexity. In this case, there is no need to deal with both parts since one knows in which part to search for N - kth less frequent element, and that reduces the average time complexity to O(N).

Algorithm

The algorithm is quite straightforward :

    Build a hash map element -> its frequency and convert its keys into the array unique of unique elements. Note that elements are unique, but their frequencies are not. That means we need a partition algorithm that works fine with duplicates.

    Work with unique array.
    Use a partition scheme (please check the next section) to place the pivot into its perfect position pivot_index in the sorted array, move less frequent elements to the left of the pivot, and more frequent or of the same frequency - to the right.

    Compare pivot_index and N - k.

        If pivot_index == N - k, the pivot is N - kth most frequent element, and all elements on the right are more frequent or of the same frequency. Return these top k frequent elements.

        Otherwise, choose the side of the array to proceed recursively.

diff

Lomuto's Partition Scheme

There is a zoo of partition algorithms. The most simple one is Lomuto's Partition Scheme, and so is what we will use in this article.

Here is how it works:

    Move the pivot at the end of the array using swap.

    Set the pointer at the beginning of the array store_index = left.

    Iterate over the array and move all less frequent elements to the left swap(store_index, i). Move store_index one step to the right after each swap.

    Move the pivot to its final place, and return this index.

Current

Implementation

Here is a total algorithm implementation.

Complexity Analysis

    Time complexity: O(N) in the average case,
    O(N2) in the worst case. Please refer to this card for a good detailed explanation of Master Theorem. Master Theorem helps to get an average complexity by writing the algorithm cost as T(N)=aT(N/b)+f(N). Here we have an example of Master Theorem case III: T(N)=T(2N​)+N, which results in O(N) time complexity. That's the case with random pivots.

    In the worst case of constantly badly chosen pivots, the problem is not divided by half at each step, it becomes just one element less, which leads to O(N2) time complexity. It happens, for example, if at each step you choose the pivot not randomly, but take the rightmost element. For the random pivot choice, the probability of having such a worst-case is negligibly small.

    Space complexity: up to O(N) to store hash map and array of unique elements.


Further Discussion: Could We Do Worst-Case Linear Time?

In theory, we could, the algorithm is called Median of Medians.

This method is never used in practice because of two drawbacks:

    It's outperformer. Yes, it works in a linear time αN, but the constant α is so large that in practice it often works even slower than N2.

    It doesn't work with duplicates.