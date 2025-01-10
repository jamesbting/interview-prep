Approach 1: Reduce to Single Word in B
Intuition

If b is a subset of a, then say a is a superset of b. Also, say N 
"a"
​
 (word) is the count of the number of "a"'s in the word.

When we check whether a word wordA in A is a superset of wordB, we are individually checking the counts of letters: that for each letter, we have N 
letter
​
 (wordA)≥N 
letter
​
 (wordB).

Now, if we check whether a word wordA is a superset of all words wordB 
i
​
 , we will check for each letter and each i, that N 
letter
​
 (wordA)≥N 
letter
​
 (wordB 
i
​
 ). This is the same as checking N 
letter
​
 (wordA)≥ 
i
max
​
 (N 
letter
​
 (wordB 
i
​
 )).

For example, when checking whether "warrior" is a superset of words B = ["wrr", "wa", "or"], we can combine these words in B to form a "maximum" word "arrow", that has the maximum count of every letter in each word in B.

Algorithm

Reduce B to a single word bmax as described above, then compare the counts of letters between words a in A, and bmax.


Complexity Analysis

Time Complexity: O(A+B), where A and B is the total amount of information in A and B respectively.

Space Complexity: O(A.length+B.length).