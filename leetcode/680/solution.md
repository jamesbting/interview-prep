Solution
Approach: Two Pointers

Intuition

Let's start by thinking about how we can solve this problem without the optional deletion included. How can we check if a given stringsis a palindrome?

    A string is a palindrome if it reads the same forward as backwards.

For a string to be a palindrome, the first and last character must be the same, the second and the second last character must be the same, and so on. An efficient way to check if a string is a palindrome is to use two pointers.

    Initialize one pointer at the start of the string and one at the end.
    Compare the characters at these pointers - if they're different, the string can't be a palindrome. If they're the same, then move the pointers towards each other.
    Continue until there is a mismatch (signifying the string is not a palindrome) or until the pointers meet each other (which would mean the string is a palindrome).

Current

We can write a handy helper functioncheckPalindrome(s, i, j)that implements this logic, wheresis the string we are checking, andiandjare the left and right bounds we want to consider. For example, to check if the entire stringsis a palindrome,iwill start at0andjwill start ats.length() - 1.

An important thing to notice is that once we verify two characters match at positionsiandj, we only care about the indicesbetween iandj. For example, withs = 'racecar', after verifying thats[0]ands[6]are the same character, we only care about indices1through5, which represent the substring'aceca'. If'aceca'is a palindrome, then'racecar'is a palindrome as well.

    For our purposes, we can basically pretend that matched characters no longer exist. For example, after verifying that the first and last characters of 'racecar' match, we can reframe the problem as checking if 'aceca' can be a palindrome with at most one deletion.

Let's assume we have some strings = 'abbxa'. On its own,sis not a palindrome. However, if we delete the'x', thensbecomes'abba', which is a palindrome. If we use the same algorithm incheckPalindrome, we will see that the first and last characters match as'a'. The pointers move inwards, and the "new" string we're focused on is'bbx'.

The next check will be a mismatch -'b' != 'x'. This means that our original string is not a palindrome. However, we can delete one character. Ifscan be a palindrome after one deletion, the deletionmustbe of one of these mismatched characters. Deleting the character'b'gives us'bx', and deleting the character'x'gives us'bb'. Because'bb'is a palindrome (which we can verify usingcheckPalindrome), the original string'abbxa'can become a palindrome with at most one character deletion.

Here's an animation that demonstrates the process using a slightly longer example:

Current

This leaves us two scenarios:

    sis a palindrome - great, we can just returntrue.

    Somewhere ins, there will be a pair of mismatched characters. Wemustuse our allowed deletion on one of these characters. Try both options - if neither results in a palindrome, then returnfalse. Otherwise, returntrue. We can "delete" the character atjby moving our bounds to(i, j - 1). Likewise, we can "delete" the character atiby moving our bounds to(i + 1, j).

Algorithm

    Create a helper functioncheckPalindromethat takes a strings, and two pointersiandj. This function returns a boolean indicating ifs.substring(i, j)is a palindrome. Implementation details for this function can be found in the first section of this article.

    Initialize two pointers,i = 0andj = s.length() - 1.

    Whilei < j, check if the characters at indicesiandjmatch. If they don't, that means we must spend our deletion on one of these characters. Try both options usingcheckPalindrome. In other words, return true if eithercheckPalindrome(s, i, j -1)orcheckPalindrome(s, i + 1, j)is true.

    If we exit the while loop, that means the original string is a palindrome. Since we didn'tneedto use the deletion, we should returntrue.

Implementation

Complexity Analysis

GivenNas the length ofs,

    Time complexity:O(N).

    The main while loop we use can iterate up toN / 2times, since each iteration represents a pair of characters. On any given iteration, we may find a mismatch and callcheckPalindrometwice.checkPalindromecan also iterate up toN / 2times, in the worst case where the first and last character ofsdo not match.

    Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means thatcheckPalindromewill never be called more than twice.

    As such, we have a time complexity ofO(N).

    Space complexity:O(1).

    The only extra space used is by the two pointersiandj, which can be considered constant relative to the input size.
