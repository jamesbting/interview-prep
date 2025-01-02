Generate Parentheses
LeetCode
142284
Aug 18, 2023
Editorial
Video Solution
Solution
Approach 1: Brute Force
Intuition

Let's start with the brute-force approach, which involves generating all possible strings of length 2n, and then verifying their validity.

img

The first step is to generate all possible strings of length 2n. We can utilize a queue data structure, queue, for implementing a breadth-first search algorithm. For each string of length i, denoted as cur_string, we will enqueue two new strings of length i + 1 by appending either ) or ( to cur_string. This process continues until the string length reaches 2n, as shown in the following figure.

img

Once we have generated a string of length 2n, the next step is to verify its validity. As a valid combination of parentheses of length 2n must have n left parentheses, with each of them matched to one of the n right parentheses to its right, we can keep track of a parameter called left_count. left_count represents the number of left parentheses that have not been matched by any right parentheses, and during iteration:

    If we encounter a left parenthesis, we increment left_count by 1.
    If we encounter a right parenthesis, we decrement left_count by 1 as it can match and "offset" one previous left parenthesis.

However, the value of left_count cannot be negative, which would mean that there is a right parenthesis without a corresponding left parenthesis to its left.

img

Finally, after traversing the entire string, we check if left_count = 0. If it is, every left parenthesis is matached to a corresponding right parenthesis, and the string is considered valid. Otherwise, it is not a valid string.

img

Algorithm

    Initialize a queue queue that contains an empty string "", create an empty array answer to store all valid strings.

    Define isValid(p_string) to check if p_string is valid by setting left_count = 0 and iterating over p_string. For each parenthesis p:
        We increment left_count by 1 if p equals (, and decrement left_count by 1 otherwise.
        If left_count < 0, return False.

    Return True if left_count = 0 after the iteration, and return False otherwise.

    Continuously dequeue strings from queue and process each dequeued string cur_string.
        If len(cur_string) = 2n, we will add it to answer if it is a valid string.
        Otherwise (len(cur_string) < 2n), we add ( or ) at the end of the cur_string and enqueue the two new strings.

    Return answer when the process ends.

Implementation
Complexity Analysis

    Time complexity: O(22n⋅n)

        We are generating all possible strings of length 2n. At each character, we have two choices: choosing ( or ), which means there are a total of 22n unique strings.

        For each string of length 2n, we need to iterate through each character to verify it is a valid combination of parentheses, which takes an average of O(n) time.

    Space complexity: O(22n⋅n)

        While we don't count the answer as part of the space complexity, for those interested, it is the nth Catalan number, which is asymptotically bounded by nn

​4n​. Thus answer takes O(n

        ​4n​) space.

        Please find the explanation behind this intuition in approach 3!
        You can also refer to Catalan number on Wikipedia for more information about Catalan numbers.

        Before we dequeue the first string of length 2n from queue, it has stored 22n−1 strings of length n−1, which takes O(22n⋅n).
        To sum up, the overall space complexity is O(22n⋅n).


Approach 2: Backtracking, Keep Candidate Valid
Intuition

    If you are not familiar with backtracking, you can refer to our Backtracking Explore Card for more information.

The previous approach of generating all possible strings of length 2n and checking each one is simple but inefficient, as it generates many invalid strings that must be checked.

A better approach is to use backtracking to generate only valid strings. This involves recursively building strings of length 2n and checking their validity as we go. In case the current string is invalid, we will not continue the recursive process on it. Instead, we will backtrack to the previous valid string on the recursive path. This approach allows us to focus only on generating valid strings, thus saving us time and resources. We continue the recursion only on the valid strings until we reach the ones of length 2n.

As shown in the picture below: ) is an invalid string, so every string prefixed with it is also invalid, and we can just drop it.

img

To ensure that the current string is always valid during the backtracking process, we need two variables left_count and right_count that record the number of left and right parentheses in it, respectively.

Therefore, we can define our backtracking function as backtracking(cur_string, left_count, right_count) that takes the current string, the number of left parentheses, and the number of right parentheses as arguments. This function will build valid combinations of parentheses of length 2n recursively.

The function adds more parentheses to cur_string only when certain conditions are met:

    If left_count < n, it suggests that a left parenthesis can still be added, so we add one left parenthesis to cur_string, creating a new string new_string = cur_string + (, and then call backtracking(new_string, left_count + 1, right_count).

    If left_count > right_count, it suggests that a right parenthesis can be added to match a previous unmatched left parenthesis, so we add one right parenthesis to cur_string, creating a new string new_string = cur_string + ), and then call backtracking(new_string, left_count, right_count + 1).

This function ensures that the generated string of length 2n is valid, and adds it directly to the answer. By only generating valid strings, we can avoid wasting time checking invalid strings.

Algorithm

    Initialize an empty list answer to store the valid strings.

    Define backtracking(cur_string, left_count, right_count) to generate valid strings recursively.
        If len(cur_string) = 2n, add it to answer and return.
        If left_count < n, add ( to cur_string and move on to backtracking(new_string, left_count + 1, right_count).
        If left_count > right_count, add ) to cur_string and move on to backtracking(new_string, left_count, right_count + 1).

    Call backtracking on empty string (backtracking("", 0, 0)) and return answer once the backtracking process is complete.

Implementation
Complexity Analysis

    Time complexity: O(n

​4n​)

    We only track the valid prefixes during the backtracking procedure. As explained in the approach 1 time complexity analysis, the total number of valid parentheses strings is O(nn

        ​4n​).

        Please find the explanation behind this intuition in approach 3!
        You can also refer to Catalan number on Wikipedia for more information about Catalan numbers.

        When considering each valid string, it is important to note that we use a mutable instance (StringBuilder in Java, list in Python etc.). As a result, in order to add each instance of a valid string to answer, we must first convert it to a string. This process brings an additional n factor in the time complexity.

    Space complexity: O(n)
        The space complexity of a recursive call depends on the maximum depth of the recursive call stack, which is 2n. As each recursive call either adds a left parenthesis or a right parenthesis, and the total number of parentheses is 2n. Therefore, at most O(n) levels of recursion will be created, and each level consumes a constant amount of space.


Approach 3: Divide and Conquer
Intuition

The problem of generating all well-formed parentheses strings of length 2n can be decomposed into smaller subproblems of generating valid strings of smaller lengths.

By leveraging the solutions to these subproblems, we can construct the solutions to the original problem. To illustrate this point, consider the following approach. Let F(n) denote the set of all valid strings of length 2n. We can construct the elements of F(n) as follows:

    Contatenating a valid string of length 0, generated by F(0), with a valid string of length 2n, generated by F(n). We can represent this concatenation as F(0)F(n) for simplicity.
    Contatenating a valid string of length 2 from F(1) with a valid string of length 2n - 2 from F(n - 1), which is equivalent to F(1)F(n - 1).
    F(2)F(n - 2).
    F(3)F(n - 3).
    ...
    F(n - 1)F(1).
    F(n)F(0).

img

However, this approach poses a problem as it involves repetitive calculations of F(n), rather than reducing the original problem into smaller subproblems.

img

By removing the outermost parentheses from the left string, we can ensure that the maximum number of parentheses pairs in the subproblem is limited to n - 1. This strategy solves the issue of redundant computation of the original problem.

img

The resulting subproblems, as depicted in the figure above, contain n - 1 pairs of parentheses in total. The inclusion of the outermost pair of parentheses from the left string results in n pairs of parentheses, which aligns with the number of pairs required in the original problem.

img

Take a look at how valid strings of length 2n are constructed in the following figure.

img

Catalan Number

    Recall that we talked about Catalan numbers earlier.
    Here we can find the connection between this number and the answer. According to the definition, the general formula for Catalan numbers is
    C(n) = C(0) * C(n - 1) + C(1) * C(n - 2) + ... + C(n - 1) * C(0)

    Looks familiar?

    We have just deduced the number of valid strings formed with n pairs of parentheses in this section (please refer to the figures above):
    F(n) = F(0)*F(n - 1) + F(1)*F(n - 2) + ... + F(n - 1)*F(0)

    We observe that this general formula matches exactly with the general formula for Catalan numbers. Therefore, the nth Catalan numbers is precisely the number of ways to form valid combinations of n pairs of parentheses.

    Note that the math behind the Catalan numbers is quite complicated and out of the scope of a technical coding interview. If an interviewer asks you to derive the time complexity for a problem like this, do your best to try and find an upper bound. Usually, backtracking solutions have very complicated time complexities that are extremely difficult to derive.


Algorithm

    If n = 0, return [""].

    Create an empty array answer = []. Iterate over the number of parentheses pairs with a variable left_count.

    Iterate over each valid string left_string from generateParenthesis(left_count).

    Iterate over each valid string right_string from generateParenthesis(n - left_count - 1).

    Construct a valid string of length 2n: We enclose left_string by a pair of parentheses, which is denoted as ( + left_string + ), then contatenate it with right_string, and add the resulting string to answer.

    Return answer when the nested iterations are complete.

Implementation
Complexity Analysis

    Time complexity: O(n

​4n​)

    We begin by generating all valid parentheses strings of length 2, 4, ..., 2n. As shown in approach 2, the time complexity for generating all valid parentheses strings of length 2n is given by the expression O(n

​4n​). Therefore, the total time complexity can be expressed T(n)=i=1∑n​i
​4i​ which is asymptotically bounded by O(n

    ​4n​).

Space complexity: O(n)

    We don't count the answer as part of the space complexity, so the space complexity would be the maximum depth of the recursion stack. At any given time, the recursive function call stack would contain at most n function calls.

