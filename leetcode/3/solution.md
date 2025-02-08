Solution Article
Overview

The primary challenge in this problem is to find an efficient way to get all possible longest substrings that contain no duplicate characters. To achieve this, we need to take advantage of Hash Table, which checks if a character occurs before quickly.

In the following three approaches, we utilize a hash table to guarantee substrings have no repeating characters and optimize the algorithm to query possible substrings step by step: the first approach is intuitive but may result in Time Limit Exceeded, and the second one uses a slide window method to narrow down the search range, and the third make further use of HashMap to reduce the search range faster.
Approach 1: Brute Force (TLE)
Intuition

Check all the substring one by one to see if it has no duplicate character.
Algorithm

Suppose we have a function boolean allUnique(String substring) which will return true if the characters in the substring are all unique, otherwise false. We can iterate through all the possible substrings of the given string s and call the function allUnique. If it turns out to be true, then we update our answer of the maximum length of substring without duplicate characters.

Now let's fill the missing parts:

    To enumerate all substrings of a given string, we enumerate the start and end indices of them. Suppose the start and end indices are i and j, respectively. Then we have 0≤i<j≤n (here end index j is exclusive by convention). Thus, using two nested loops with i from 0 to n−1 and j from i+1 to n, we can enumerate all the substrings of s.

    To check if one string has duplicate characters, we can use a set. We iterate through all the characters in the string and put them into the set one by one. Before putting one character, we check if the set already contains it. If so, we return false. After the loop, we return true.

Implementation
Complexity Analysis

    Time complexity : O(n3).

    To verify if characters within index range [i,j) are all unique, we need to scan all of them. Thus, it costs O(j−i) time.

    For a given i, the sum of time costed by each j∈[i+1,n] is

    ∑i+1n​O(j−i)

    Thus, the sum of all the time consumption is:

    O(∑i=0n−1​(∑j=i+1n​(j−i)))=O(∑i=0n−1​2(1+n−i)(n−i)​)=O(n3)

    Space complexity : O(min(n,m)). We need O(k) space for checking a substring has no duplicate characters, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.

Approach 2: Sliding Window
Intuition

Given a substring with a fixed end index in the string, maintain a HashMap to record the frequency of each character in the current substring. If any character occurs more than once, drop the leftmost characters until there are no duplicate characters.
Algorithm

The naive approach is very straightforward. But it is too slow. So how can we optimize it?

In the naive approaches, we repeatedly check a substring to see if it has duplicate character. But it is unnecessary. If a substring sij​ from index i to j−1 is already checked to have no duplicate characters. We only need to check if s[j] is already in the substring sij​.

To check if a character is already in the substring, we can scan the substring, which leads to an O(n2) algorithm. But we can do better.

By using HashSet as a sliding window, checking if a character in the current can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j) (left-closed, right-open). A sliding window is a window "slides" its two boundaries to the certain direction. For example, if we slide [i,j) to the right by 1 element, then it becomes [i+1,j+1) (left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current window [i,j) (j=i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.
Implementation
Complexity Analysis

    Time complexity : O(2n)=O(n). In the worst case each character will be visited twice by i and j.

    Space complexity : O(min(m,n)). Same as the previous approach. We need O(k) space for the sliding window, where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.

Approach 3: Sliding Window Optimized
Intuition

The above solution requires at most 2n steps. In fact, it could be optimized to require only n steps. Instead of using a set to tell if a character exists or not, we could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
Algorithm

The reason is that if s[j] have a duplicate in the range [i,j) with index j′, we don't need to increase i little by little. We can skip all the elements in the range [i,j′] and let i to be j′+1 directly.

Here is a visualization of the above code.
Implementation