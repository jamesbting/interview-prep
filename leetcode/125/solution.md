Approach 1: Compare with Reverse

Intuition

A palindrome is a word, phrase, or sequence that reads the same backwards as forwards. e.g. madam

A palindrome, and its reverse, are identical to each other.

Algorithm

We'll reverse the given string and compare it with the original. If those are equivalent, it's a palindrome.

Since only alphanumeric characters are considered, we'll filter out all other types of characters before we apply our algorithm.

Additionally, because we're treating letters as case-insensitive, we'll convert the remaining letters to lower case. The digits will be left the same.

Complexity Analysis

    Time complexity : O(n), in length n of the string.

    We need to iterate thrice through the string:
        When we filter out non-alphanumeric characters, and convert the remaining characters to lower-case.
        When we reverse the string.
        When we compare the original and the reversed strings.

    Each iteration runs linear in time (since each character operation completes in constant time). Thus, the effective run-time complexity is linear.

    Space complexity : O(n), in length n of the string. We need O(n) additional space to stored the filtered string and the reversed string.


Approach 2: Two Pointers

Intuition

If you take any ordinary string, and concatenate its reverse to it, you'll get a palindrome. This leads to an interesting insight about the converse: every palindrome half is reverse of the other half.

Simply speaking, if one were to start in the middle of a palindrome, and traverse outwards, they'd encounter the same characters, in the exact same order, in both halves!

Current

Algorithm

Since the input string contains characters that we need to ignore in our palindromic check, it becomes tedious to figure out the real middle point of our palindromic input.

    Instead of going outwards from the middle, we could just go inwards towards the middle!

So, if we start traversing inwards, from both ends of the input string, we can expect to see the same characters, in the same order.

The resulting algorithm is simple:

    Set two pointers, one at each end of the input string
    If the input is palindromic, both the pointers should point to equivalent characters, at all times. 1
        If this condition is not met at any point of time, we break and return early. 2
    We can simply ignore non-alphanumeric characters by continuing to traverse further.
    Continue traversing inwards until the pointers meet in the middle.

Complexity Analysis

    Time complexity : O(n), in length n of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.

    Space complexity : O(1). No extra space required, at all.

Footnotes

    Such a property is formally known as a loop invariant. ↩

    Such a property is often called a loop termination condition. It is one of several used in this solution. Can you identify the others? ↩
