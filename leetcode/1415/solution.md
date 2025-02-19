Solution
Overview
We are given a positive integern, which represents the length of the string, and an integerk. Our task is to find thek 
th
 happy string of lengthnwhen allhappystrings are listed in lexicographical order. Let’s break this down:

Happy Strings: A string is called happy if it consists only of the characters'a','b', and'c', and no two consecutive characters are the same. For example,"abc"and"aba"are happy strings, but"aa"and"ad"are not.

Lexicographical Order: This is the order in which words appear in a dictionary. When comparing two strings, we look at the first different character. The one with the smaller character (closer to'a'in the alphabet) comes first. For example,"abc"comes before"acb"because'b'comes before'c'.

Note: If there are fewer thanksuch strings, we return an empty string.

Approach 1: Backtracking
Intuition
In this approach, we will use backtracking to simulate the described process and generate all happy strings of sizen. To do this, we will build the strings step by step while ensuring they follow the "happy" property.

For a more comprehensive understanding of backtracking, check out theBacktracking Explore Card 🔗. This resource provides an in-depth look at recursion and backtracking, explaining its key concepts and applications with a variety of problems to solidify understanding of the pattern.

We start with an empty string and recursively extend it by adding characters'a','b', or'c', making sure that no two consecutive characters are the same. This means that at each step, we choose a character that is different from the last one in the string. To implement this, we iterate over the characters'a','b'and'c'and for each of them we check whether it matches the last character of the string we have constructed so far (currentString.back()). If so, we skip this character. Otherwise, we add it to the end of thecurrentStringand continue the backtracking by callinggenerateHappyString(n, currentString + currentChar, happyStrings).

After generating all happy strings of sizen, we check if there are at leastkof them. If there are, we sort these strings in lexicographical order and return thek 
th
 one. Otherwise, we return an empty string to indicate that there are not enough happy strings.

Algorithm
In thegenerateHappyStrings(n, currentString, happyStrings)function:
If we have reached the desired string length, i.e.,currentString.size() == n:
PushcurrentStringintohappyStringsand return.
Iterate over the candidate characters withcurrentCharfrom'a'to'c':
IfcurrentCharis the same as the last character in thecurrentString, skip it.
Recursively callgenerateHappyString(n, currentString + currentChar, happyStrings).
In the maingetHappyStringfunction:
InitializecurrentStringto an empty string.
Initialize an arrayhappyStringsto store all happy strings of lengthn.
CallgenerateHappyStrings(n, currentString, happyStrings)to generate the happy strings starting from the empty string.
If there are less thankhappy strings of lengthn, i.e.,happyStrings.size() < k, return an empty string.
SorthappyStringsin lexicographic order.
Return thek-thhappy string, i.e.,happyStrings[k - 1].
Implementation

Complexity Analysis
Letnbe the desired length of the happy strings.

Time Complexity:O(n⋅2 
n
 ).

In the backtracking, we explore 3 options for the first character of the string and 2 options for the next character at each of the following steps. This is similar to exploring all nodes in a binary tree withnlevels, resulting in a time complexity ofO(2 
n
 )for generating the strings. Then, we sort3⋅2 
n−1
 =O(2 
n
 )strings, which requires2 
n
 log2 
n
 =O(n⋅2 
n
 )time.

Thus, the overall complexity is determined by the sorting of all happy strings and is equal toO(n⋅2 
n
 ).

Space Complexity:O(2 
n
 ).

We create an array to store all happy strings of lengthn, which will eventually hold3⋅2 
n−1
 =O(2 
n
 )elements. Additionally, the recursion depth can grow up ton, adding anotherO(n)factor to the total space complexity. However, the amount of extra space used is dominated by thehappyStringsarray and remains equal toO(2 
n
 ).

Approach 2: Optimized Recursion
Intuition
Building on the previous approach, we will again generate happy strings of lengthnby extending an already happy string until it reaches the desired size. However, there's a key observation: the order in which we generate the strings is not random.

Since we add characters in alphabetical order, we naturally explore all strings starting with'a'before backtracking and moving to those starting with'b', and so on. This means the strings are generated directly in lexicographical order.

Because of this, we don't need to store all the strings and sort them later. Instead, we can keep a counter - corresponding to the index of the current string in the sorted list - to track how many strings we've generated. When we reach thek 
th
 string, we store it as the result and stop the process, saving both time and space.

Algorithm
In thegenerateHappyStrings(n, k, currentString, indexInSortedList, result)function:
If we have reached the desired string length, i.e.,currentString.size() == n:
IncrementindexInSortedListby1.
If we have reached thek-thstring, i.e.,indexInSortedList == k, storecurrentStringinresult.
Otherwise, extend the current string by iterating over the candidate characters withcurrentCharfrom'a'to'c':
IfcurrentCharis the same as the last character in thecurrentString, skip it.
Otherwise, add it to the end ofcurrentString.
Recursively callgenerateHappyString(n, k, currentString, indexInSortedList, result).
If we have found thek-thstring during this traversal, i.e.,resultis not an empty string, return.
Remove the last character ofcurrentStringto backtrack with the next one.
In the maingetHappyStringfunction:
InitializecurrentStringandresultto empty strings.
InitializeindexInSortedListto0.
CallgenerateHappyStrings(n, k, currentString, indexInSortedList, result)to generate the happy strings starting from the empty string.
Returnresult.
Implementation

Complexity Analysis
Letnbe the length of the happy strings andkthe index of the result string in the sorted list.

Time Complexity:O(k⋅n)orO(n⋅2 
n
 ).

The algorithm generates happy strings in lexicographical order using backtracking and stops when thek 
th
 one is found.

In the worst case, the algorithm generatesmin(k,3⋅2 
n−1
 )strings before terminating. For each string, it performsnrecursive calls (one for each character in the string) and each of them involves only constant-time operations such as checking if the current character is valid and updating the current string.

Therefore, the total time complexity of the algorithm isO(k⋅n)orO(n⋅2 
n
 )the number of strings generated isO(2 
n
 ).

Space Complexity:O(n).

Regarding additional space usage, we maintain a stringcurrentStringfor backtracking, which can grow up to sizen. Since this string is passed by reference in the recursive function, no extra copies are created, keeping its space usage atO(n).

Additionally, the recursion depth is alsoO(n)because we make a recursive call for each of thencharacters in the string.

Thus, the overall space complexity isO(n).

Approach 3: Iterative Using a Stack
Intuition
Recursive solutions are often more intuitive for backtracking but can be inefficient due to uncontrolled stack growth. Each recursive call adds a new frame to the call stack, storing local variables and execution details, which can lead to excessive memory usage or even a stack overflow. To avoid this, we will use our own stack to simulate recursion, giving us greater control over memory usage and preventing unnecessary overhead. Feel free to refer to the relativeLeetCode Explore Cardfor a more detailed overview of the stack data structure.

So, instead of making a new function call every time we extend thecurrentString, we store the next string to be processed (i.e.,currentString + currentChar) in a stack. Then, retrieving a string from the top of the stack is the same as entering the function call that would have this string ascurrentString. The logic from this point remains the same: we go over all valid characters and try to extend the current string by adding them to the end of it. However, it is important to note that the string at the top of the stack is the one that will be processed (or expanded) first. Therefore, we need to push, for example, the string"abca"onto the stack after"abcb"so that it is retrieved first, ensuring that the strings are generated in lexicographic order. To achieve this, we will extend the current string by starting from the last valid character ('c') and iterating backward to the first ('a').

Algorithm
Initialize an empty stack,stringsStack.
InitializeindexInSortedListto0.
Push the empty string into thestringsStack.
While thestringsStackis not empty:
Pop the top element of the stack ascurrentString.
If thecurrentStringhas a length equal ton:
IncrementindexInSortedListby1.
If this is thek-thstring in lexicographical order, i.e.,indexInSortedList == k, return it.
Otherwise, extend the current string by iterating over the valid characters in reversed order, i.e., withcurrentCharfrom'c'to'a':
If the current string is not empty andcurrentCharis equal to its last character, skip it.
AddcurrentString + currentCharto the stack.
If the traversal ends and thek-thhappy string is not found, there are less thankhappy strings of lengthn, so return an empty string.
Implementation

Complexity Analysis
Letnbe the length of the happy strings andkthe index of the result string in the sorted list.

Time Complexity:O(k⋅n)orO(n⋅2 
n
 ).

As in the previous approach, we generatemin(k,3⋅2 
n−1
 )strings of lengthn, so the loop will run forO(k⋅n)orO(n⋅2 
n
 )times. Extending the current string by one character involves only constant-time operations, like iterating over the 3 valid characters and pushing the next string onto the top of the stack. Therefore, the total time complexity of the algorithm isO(k⋅n)orO(n⋅2 
n
 ).

Space Complexity:O(n 
2
 ).

The algorithm uses an explicit stack (stringsStack) to perform backtracking. During the traversal to construct the lexicographically smallest happy string ("ababa..."), we continuously extend a string of the form"ababa...". At each level of recursion, we also push alternative choices onto the stack, such as"ababc", which represent different branches of the search.

When we reach a valid happy string of lengthn, the stack containsO(n)stored strings at most, each of which can beO(n)in length. Therefore, the total space complexity of the algorithm, determined by the size of the stack, isO(n 
2
 ).

Approach 4: Combinatorics
Intuition
The main idea of this approach is that we do not need to generate allk−1happy strings to find thek 
th
 smaller one. To better understand this, let's make the following observations:

The total number of happy strings of lengthnis3⋅2 
n−1
 . This is because the first character has 3 choices ('a','b', or'c') and each subsequent character has 2 choices, as it must differ from the preceding character. Therefore, ifkexceeds this total, it implies that thek-th happy string does not exist, and we should return an empty string.

Moving on to the harder case, note that the set of all happy strings can be divided into three equal groups based on their starting character:

Strings starting with'a': positions1to2 
n−1
 .
Strings starting with'b': positions2 
n−1
 +1to2⋅2 
n−1
 .
Strings starting with'c': positions2⋅2 
n−1
 +1to3⋅2 
n−1
 .
Each group contains2 
n−1
 strings, as fixing the first character leaves2 
n−1
 ways to choose the remaining characters. By comparingkto these ranges, we can determine the first character of the desired string and adjustkto reflect its position within the subgroup by subtracting the group's starting index.

Similarly, every subsequent character at thei 
th
 position divides the strings of its group into two subgroups of size2 
n−i−1
 :

Strings starting with the smallest valid character ('a'->'b','b'->'a'and'c'->'a').
Strings starting with the greatest valid character ('a'->'c','b'->'c'and'c'->'b').
By comparingkwith the midpoint at which the groups are split, i.e.,2 
n−i−1
 , we can determine whether the result string belongs to the first or last subgroup and set the character at positioniaccordingly.

Algorithm
Calculate the total number of happy strings of lengthnastotal = 3 * pow(2, n - 1).
Ifkis greater thantotal, return an empty string.
Initialize theresultstring.
Initialize two maps,nextSmallestandnextGreatest, that map each of the three characters to the smallest and largest characters respectively that can go after them.
Set the index of the first string that starts with'a'(startA) to1(the lexicographically smallest happy string with'a').
Calculate the index of the first string that starts with'b'asstartB = startA + pow(2, n - 1).
Calculate the index of the first string that starts with'c'asstartC = startB + pow(2, n - 1).
Determine the first character of the string:
Ifkis less thanstartB, set the first character ofresultto'a'and subtractstartAfromk.
Else ifkis less thanstartC, set the first character ofresultto'b'and subtractstartBfromk.
Else, set the first character ofresultto'c'and subtractstartCfromk.
For each subsequent character, atcharIndex:
Calculate themidpointof its group, asmidpoint = pow(2, n - charIndex - 1).
Ifkis less thanmidpoint, setresult[charIndex] = nextSmallest[result[charIndex - 1]]to extendresultwith the smallest valid character.
Otherwise:
Setresult[charIndex] = nextGreatest[result[charIndex - 1]].
Decrementkbymidpointso that it corresponds to the index of the result string within the current group.
Returnresult.
Implementation

Complexity Analysis
Letnbe the length of the happy strings.

Time Complexity:O(n).

We construct the result string by iterating over its characters and determining each of them in constant time. Therefore, the time complexity of this algorithm isO(n).

Space Complexity:O(1).

Excluding the output string, the algorithm only requires a fixed number of variables and two maps (nextGreatestandnextSmallest) of fixed size. Thus, the auxiliary space complexity is constant orO(1).

