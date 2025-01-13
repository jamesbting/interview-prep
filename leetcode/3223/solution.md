Solution
Overview

We are given a string s. The goal is to repeatedly perform the following operation until it is no longer possible:

    Choose an index i such that:
        There is at least one character equal to s[i] to its left.
        There is at least one character equal to s[i] to its right.
    Once such an index is found, the following characters are removed:
        The closest matching character to the left of index i.
        The closest matching character to the right of index i.

We need to find the smallest possible length of the string after applying this operation repeatedly.
Approach 1: Using Hash Map
Intuition

To approach this problem, we need to consider how often each character appears in the string. The goal is to figure out how many characters need to be removed to minimize the string, based on how many times each character occurs:

    If a character appears an odd number of times, we can keep exactly one instance of it, and remove the rest.
    If a character appears an even number of times, we can keep two instances of it—one on the left side and one on the right side, ensuring a valid operation.

For example, let's consider the case where we have 5 'a' characters. Since 5 is odd, we'll end up with exactly one 'a'. We can remove the first and third 'a' characters because they are closest to the second 'a'. After that, we are left with three 'a' characters, and we repeat the process of removing pairs. In the end, only one 'a' remains. This is because each pair cancels out, leaving the extra character.

Now, let's look at the case with 4 'a' characters. Since 4 is even, we first remove the first and third 'a' characters, which are closest to the second 'a'. We're left with 2 'a' characters, but for comparisons, we need three characters: one as the reference pivot and two indices, one on the left and one on the right, to remove. So, we stop here in the even case.

The entire intuition can be summarized with the help of the image below.

odd_even_cancellation
Algorithm

    Count the frequency of each character in the string:
        Initialize a frequency map (charFrequencyMap).
        For each character in the string s, increment its frequency in the map.

    Calculate the number of characters to delete:
        Initialize deleteCount to 0.
        For each character's frequency in the map:
            If the frequency is odd, add frequency - 1 to deleteCount (remove all but one).
            If the frequency is even, add frequency - 2 to deleteCount (remove all but two).

    Return the smallest length of the string after deletions:
        Subtract deleteCount from the original string length.

Implementation
Complexity Analysis

Let n be the size of the string s, and let k be the size of the character set.

    Time Complexity: O(n)

    The first loop iterates over each character in the string s, which takes O(n) time. This is because inserting or updating elements in an map has an average time complexity of O(1) per operation. The second loop iterates over the charFrequencyMap, which has at most k unique characters. This loop takes O(k) time. Since k is typically much smaller than n (e.g., k=26 for lowercase letters), the overall time complexity is dominated by the first loop, resulting in O(n).

    Space complexity: O(1) or O(k)

    The space used by the charFrequencyMap depends on the size of the character set k. In our case, k is fixed (e.g., 26 for lowercase letters), so the space complexity is O(1). Alternatively, it can also be expressed as O(k).

Approach 2: Using Frequency Array
Intuition

In the previous approach, we used a hash map to count how often each character appears in the string. Hash maps are flexible and can handle cases where the characters are not limited to a specific set. However, they come with some downsides.

A hash map uses a dynamic data structure, which requires extra memory to store keys and values. This leads to higher space usage compared to an array. Additionally, the process of hashing (calculating a unique code for each character) takes time. While hash map operations like insertion and lookup are generally fast (on average, they take O(1) time), they can sometimes be slower due to hashing collisions (when two keys produce the same hash) and memory allocation.

In this problem, we only need to deal with lowercase English letters ('a' to 'z'). Since there are only 26 possible characters, we can use a fixed-size array of size 26 to count character frequencies.

To achieve this, we use a simple hashing operation to map each character to a position in a frequency array. In ASCII, each lowercase letter can be represented as the value of 'a' plus its index in the alphabet. By subtracting the ASCII value of 'a' from any character, we get a unique integer between 0 and 25, which corresponds to its position in the frequency array.

This approach is more efficient for this specific case because of two reasons.

    Better Runtime: When we access an element in an array, it’s always a constant time operation. On the other hand, hash maps are O(1) on average, but they can occasionally slow down because of the hashing process or when collisions happen.
    Space Efficiency: An array of size 26 uses a fixed, small chunk of memory. Unlike hash maps, arrays don’t need additional structures like hash buckets or key-value pairs, so they’re much more memory-efficient.

Apart from using this array, the key idea remains the same as the previous approach:

    If a character appears an odd number of times, we keep one instance.
    If a character appears an even number of times, we keep two instances.

Algorithm

    Initialize a charFrequency array of size 26 to store the count of occurrences for each character in the string.

    Initialize totalLength to 0, which will hold the final result.

    Iterate through each character currentChar in string s:
        Increment the corresponding index (currentChar - 'a') in charFrequency based on currentChar.

    Calculate the total length of characters that will remain:
        Iterate through each frequency in charFrequency:
            If frequency is 0, skip the character (it doesn't appear in the string).
            If frequency is even, add 2 to totalLength.
            If frequency is odd, add 1 to totalLength.

    Return totalLength, the smallest length of the string after deletions.

Implementation
Complexity Analysis

Let n be the size of the string s, and let k be the size of the character set.

    Time complexity: O(n)

    The first loop iterates over each character in the string s, which takes O(n) time. The second loop iterates over the charFrequency array, which has a size of k. This loop runs in O(k) time. Since k is typically a constant, the second loop is often considered O(1). However, in the general case, the time complexity is O(n+k). For most practical purposes, k is small compared to n, so the overall time complexity is dominated by O(n).

    Space complexity: O(1) or O(k)

    The space used by the charFrequency depends on the size of the character set k. In our case, k is fixed (e.g., 26 for lowercase letters), so the space complexity is O(1). Alternatively, it can also be expressed as O(k).
