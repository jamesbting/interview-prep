Solution
Approach 1: Iteration
Intuition
We are given a string s and a substring part, and we need to repeatedly remove the first occurrence of part from s until it no longer appears. Since the constraints are relatively small (s.length <= 1000 and part.length <= 1000), we can try a brute force approach.

We can use a simple iterative approach which loops through s as long as part is present in it. Each time we find part, we need to remove its first occurrence. To do this, we first locate the leftmost occurrence of part in s. Once we know where it starts, we can break s into three sections: the part of the string before the occurrence of part, the occurrence of part itself, and the part of the string after part. By combining the first and third sections (effectively leaving out the middle section), we remove that occurrence of part from s.

When the loop finishes, s will no longer contain any occurrences of part, so we return it as the result.

It’s worth noting that we can simplify this process by utilizing built-in string methods provided by the programming language.
For instance, in Java, the String.replaceFirst method can be used to replace the first occurrence of a substring, in Python3 we can use str.replace, and in C++ we can use a combination of std::string::erase and std::string::find.
Most of the time, it is beneficial to use these built-in functions since they are heavily optimized and tested, and will almost always perform better than our own implementations.

Algorithm
Run a while loop to repeatedly check if the string s contains the substring part.
Find the index of the leftmost occurrence of part in s and store it in a variable partStartIndex.
Use the substring method to extract the portion of s before part (s.substring(0, partStartIndex)) and the portion after part (s.substring(partStartIndex + part.length())).
Concatenate the first and last portions and assign it back to s.
Return the updated string s, which no longer contains any occurrences of part.
Implementation

Complexity Analysis
Let n be the length of the string s and m be the length of the substring part.

Time complexity: O(n 
2
 /m)

The algorithm uses a while loop to repeatedly remove the leftmost occurrence of part from s. Each iteration of the loop involves finding the index of part, which takes O(n) time, and then creating a new string by concatenating the segments before and after part, which also takes O(n) time. In the worst case, there are O(n/m) such iterations (e.g., when part is non-overlapping and removed sequentially). The total time across all iterations is O(n⋅(n/m))=O(n 
2
 /m).

Space complexity: O(n)

Although the algorithm does not explicitly use additional data structures, each iteration creates a new string by concatenating the segments before and after part. This results in the creation of intermediate strings, each of size up to O(n). The space required to store these intermediate strings dominates the space complexity, leading to O(n) space usage.

Approach 2: Stack
Intuition
In the first approach, we relied on built-in methods to find and remove substrings. Let’s explore how to implement this functionality entirely on our own.

One issue with repeatedly removing substrings from a string is that it requires recreating the entire string every time. We need a way such that removing the substring characters from a string at any point is as close to constant time as possible.

We can simulate this using a stack. A stack allows us to remove its topmost element in constant time. So, if we incrementally put the characters of s in the stack, the moment we find out that the last part of the stack forms part, we simply pop the entire substring out. This means we needed to only loop over the length of part, rather than the entire string s.

To implement this, we can loop over each character of s and add it to the stack. As we add characters, we constantly check if the most recent portion of the stack matches the substring part. If it does, we remove those characters from the stack. This approach avoids scanning the entire string repeatedly and only focuses on the portions of s that could potentially contain part.

However, if at any point the characters don’t match, it means that the stack doesn’t contain part at the top. In that case, any intermediate pops made during the check need to be undone, so the characters are pushed back onto the stack in the correct order. The process continues for the rest of the string.

When we finish processing all the characters in s, the stack will contain the modified version of s with all occurrences of part removed. At this point, the stack’s contents are reversed compared to the original string, so we reverse them back to produce the final result, which is then returned.

For a more comprehensive understanding of stacks, check out the Stack Explore Card 🔗. This resource provides an in-depth look at stacks, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

Algorithm
Initialize a stack of characters stk to store the characters of the string as they are processed.
Calculate the lengths of the input string s and the substring part, storing them in strLength and partLength, respectively.
Use a for loop to iterate through each character in the string s, starting from index 0 and ending at strLength - 1.
Push the current character of the string onto the stack.
Check if the size of the stack is greater than or equal to partLength. If so:
Use the helper method checkMatch to check if the top of the stack matches part:
If a match is found, pop the top partLength characters from the stack.
After processing the entire string, initialize a string result to construct the resulting string.
While the stack is not empty, pop each character from the stack and append it to the result.
Reverse the order of result to correct the sequence of characters and return it.
Helper method checkMatch(stk, part, partLength):

Initialize a temporary stack temp and copy all characters from the original stack stk into temp.
Use a for loop to iterate over part in reverse order, starting from index partLength - 1 and ending at 0. For each character:
Compare the current character of part with the top character of temp:
If they do not match, return false.
Else, remove the top character from temp.
If all characters of part match the top characters of the stack in reverse order, return true.
Implementation

Complexity Analysis
Let n be the length of the string s, and m be the length of the substring part.

Time complexity: O(n⋅m)

The algorithm iterates through each character of the string s, contributing O(n) to the complexity. For each character pushed onto the stack, the algorithm checks if the top m characters of the stack match part. This involves an O(m) comparison for potential matches. Since this check can occur for each character in s, the worst-case time complexity is O(n⋅m).

Space complexity: O(n+m)

The stack stores up to O(n) characters in the worst case (e.g., when no part substrings are removed). The temporary stack temp in the checkMatch function also requires O(n) space. Additionally, the potentialMatch string temporarily stores up to O(m) characters during each iteration. So, the total space complexity is O(n) (stacks) + O(m) (temporary potentialMatch), which simplifies to O(n+m).

Approach 3: Knuth-Morris-Pratt (KMP) Algorithm
Intuition
So far, we have relied on a naive approach for pattern matching, where we slide the pattern (part) over the string (s) one character at a time and check for a match. For example, if s = "ABABDABACDABABCABAB" and part = "ABABCABAB", the naive approach compares part with every substring of s of the same length, often rechecking characters unnecessarily. Consider the scenario where the first four characters, "ABAB", match, but a mismatch occurs with the fifth character. In the naive approach, the pattern is shifted by just one character, and the comparison restarts from the beginning of part, rechecking "BAB" again. This results in redundant comparisons and inefficiency.

The Knuth-Morris-Pratt (KMP) algorithm optimizes this by using a longest prefix-suffix (LPS) array for the pattern. The LPS array helps determine how much of the pattern has been matched so far, allowing the algorithm to skip redundant comparisons. When a mismatch happens, instead of starting over from the beginning, we use the LPS array to shift the pattern by an appropriate amount.

For example, if we’ve matched "ABABC" but encounter a mismatch at the 6th character, the LPS value for "ABABC" is 1. We then shift the pattern by 4 characters (5 – 1) and continue matching. This avoids rechecking parts of the pattern we’ve already matched.

For example, consider the pattern part = "ABABCABAB". Let's see how we build up the LPS array in the slideshow below:

Current

The LPS array allows the KMP algorithm to skip unnecessary comparisons when a mismatch occurs. When a mismatch happens, instead of starting over from the beginning of the pattern, the algorithm uses the LPS array to determine how much of the pattern has already been matched. It then shifts the pattern by an appropriate amount and continues matching.

For example, let’s say we’re matching part = "ABABCABAB" against s = "ABABDABACDABABCABAB". Suppose we’ve matched the first 5 characters ("ABABC") but encounter a mismatch at the 6th character. The LPS value for the prefix "ABABC" is 1, so we know that the first 1 character of the pattern ("A") is already matched. Instead of starting over, we shift the pattern by 4 characters (length of the matched prefix minus the LPS value: 5 - 1 = 4) and continue matching. This skipping of unnecessary comparisons makes the KMP algorithm much more efficient.

The LPS array is built using a linear iterative approach. We initialize two pointers: current (to traverse part) and prefixLength (to track the length of the matching prefix-suffix). We then iterate through the pattern:

If the characters at current and prefixLength match, we increment both pointers and set lps[current] = prefixLength.
If they don’t match and prefixLength is not zero, we backtrack prefixLength to lps[prefixLength - 1].
If they don’t match and prefixLength is zero, we set lps[current] = 0 and increment current.
Here's a slideshow to visualize this process better:

Current

Finally, we process each character of s while using the LPS array to track how much of part has been matched. We iterate over s and when a complete match is found, we remove the matched substring from the stack. If a mismatch occurs, we use the LPS array to backtrack and continue matching.

After processing all characters of s, the stack contains the characters of s with all occurrences of part removed. We convert the stack into a string by popping characters and reversing the result (since stacks are last-in-first-out). We return this result as our answer.

Algorithm
Call the helper method computeLongestPrefixSuffix with the substring part to calculate the Longest Prefix Suffix (LPS) array.
Create a stack charStack to store characters of the string s as they are processed.
Declare an array patternIndexes of size s.length() + 1 to keep track of the pattern index for each character in the stack.
Use a for loop to iterate through each character in the string s. Also, maintain a variable patternIndex to track the current position in the substring part.
Push the current character onto the stack.
If the current character matches the character at patternIndex in part:
Increment patternIndex and store it in patternIndexes[charStack.size()].
If patternIndex equals the length of part, the pattern is fully matched:
Pop part.length() characters from the stack to remove the matched pattern.
Reset patternIndex to patternIndexes[charStack.size()] if the stack is not empty, otherwise set it to 0.
If the current character does not match the character at patternIndex in part:
If patternIndex is not 0, backtrack by setting patternIndex to lps[patternIndex - 1] and decrement strIndex to reprocess the current character.
If patternIndex is 0, set patternIndexes[charStack.size()] to 0.
Initialize result to construct the result string from the remaining characters in the stack.
Reverse the constructed string and return it as the output.
Helper method computeLongestPrefixSuffix(pattern)

Create an array lps of size equal to the length of the pattern part to store the lengths of the longest proper prefix which is also a suffix.
Use a for loop to traverse the pattern part starting from index 1. Maintain a variable prefixLength to track the length of the longest prefix-suffix.
If the character at the current position matches the character at prefixLength:
Increment prefixLength and store it in lps[current].
Proceed to the next character.
Else if the characters do not match and prefixLength is non-zero:
Backtrack to the previous longest prefix-suffix using the LPS array.
If no match is found and prefixLength is zero, set lps[current] to zero and proceed to the next character.
Return the fully constructed lps array.
Implementation

Complexity Analysis
Let n be the length of the string s, and m be the length of the substring part.

Time complexity: O(n+m)

The algorithm consists of two main components: the preprocessing step to compute the KMP longest prefix-suffix (lps) array and the traversal of the string s.

The preprocessing step takes O(m) time, as the lps array is computed for the pattern part.

The traversal of s uses a stack and performs efficient pattern matching with the help of the lps array. Each character in s is processed once, and backtracking in the pattern matching is guided by the lps array, ensuring that each character is examined only a constant number of times. Thus, the traversal takes O(n) time.

Combining these two components, the overall time complexity is O(n+m).

Space complexity: O(n+m)

The primary space usage comes from the stack, which can store up to n characters in the worst case if no matches are removed. Additionally, the pattern matching indices array requires O(n) space, and the lps array used for KMP preprocessing requires O(m) space. These components together result in a total space complexity of O(n+m).