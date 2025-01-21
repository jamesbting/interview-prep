Overview
Data Structure Trie

This article introduces the data structure trie. It could be pronounced in two different ways: as "tree" or "try". Trie which is also called a digital tree or a prefix tree is a kind of search-ordered tree data structure mostly used for the efficient dynamic add/search operations with the strings.

Trie is widely used in real life: autocomplete search, spell checker, T9 predictive text, IP routing (longest prefix matching), some GCC containers.

Here is what it looks like

fig

Figure 1. Data structure trie.

There are two main types of trie interview questions:

    Standard Trie. Design a structure to dynamically add and search strings, for example

        Add and Search Word.

        Word Search II.

        Design Search Autocomplete System.

    Bitwise Trie. Design a structure to dynamically add binary strings and compute maximum/minimum XOR/AND/etc, for example
        Maximum XOR of Two Number in an Array.

Why Trie and not HashMap

It's quite easy to write the solution using such data structures as hashmap or balanced tree.

This solution passes all LeetCode test cases and formally has O(M⋅N) time complexity for the search, where M is the length of the word to find, and N is the number of words. Although this solution is not efficient for the most important practical use cases:

    Finding all keys with a common prefix.

    Enumerating a dataset of strings in lexicographical order.

    Scaling for the large datasets. Once the hash table increases in size, there are a lot of hash collisions and the search time complexity could degrade to O(N2⋅M), where N is the number of the inserted keys.

    Trie could use less space compared to hashmap when storing many keys with the same prefix. In this case, using trie has only O(M⋅N) time complexity, where M is the key length, and N is the number of keys.



Approach 1: Trie

How to Implement Trie: addWord function

fig

Figure 2. Trie implementation.

In trie, each path from the root to the "word" node represents one of the input words, for example, o -> a -> t -> h is "oath".

Trie implementation is pretty straightforward, it's basically nested hashmaps. At each step, one has to verify, if the child node to add is already present. If yes, just go one step down. If not, add it into the trie and then go one step down.

Current

Complexity Analysis

    Time complexity: O(M), where M is the key length. At each step, we either examine or create a node in the trie. That takes only M operations.

    Space complexity: O(M). In the worst-case newly inserted key doesn't share a prefix with the keys already inserted in the trie. We have to add M new nodes, which takes O(M) space.

Search in Trie

In the absence of '.' characters, the search would be as simple as addWord. Each key is represented in the trie as a path from the root to the internal node or leaf. We start from the root and go down in trie, checking character by character.

fig

Figure 3. Search in trie.

The presence of '.' characters forces us to explore all possible paths at each . level.

fig

Figure 4. Search in trie.

Complexity Analysis

    Time complexity: O(M) for the "well-defined" words without dots, where M is the key length, and N is a number of keys, and O(N⋅26M) for the "undefined" words. That corresponds to the worst-case situation of searching an undefined word M times

    .........​​ which is one character longer than all inserted keys.

    Space complexity: O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words, to keep the recursion stack.

Implementation