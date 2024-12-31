import java.util.*;
class Trie {

    private static final char END_OF_WORD = '|';

    private Map<Character, TrieNode> roots;

    private class TrieNode {
        private final char c;
        private final Map<Character, TrieNode> adjacent;

        TrieNode(final char c) {
            this.c = c;
            this.adjacent = new HashMap<>();
        }

        void insert(String word) {
            if (word.length() < 1) {
                return;
            }   

            char c = word.charAt(0);
            if (!this.adjacent.containsKey(c)) {
                TrieNode nextLetter = new TrieNode(c);
                this.adjacent.put(c, nextLetter);
            }
            this.adjacent.get(c).insert(word.substring(1, word.length()));
        }

        boolean search(String word) {
            if (word.length() == 1) {
                return this.c == END_OF_WORD && this.c == word.charAt(0);
            }
            char c = word.charAt(0);
            char next = word.charAt(1);
            return this.c == c && 
                this.adjacent.containsKey(next) && 
                this.adjacent.get(next).search(word.substring(1, word.length()));
        }

        boolean startsWith(String prefix) {
            if (prefix.length() == 2) {
                return this.c == prefix.charAt(0);
            }

            char c = prefix.charAt(0);
            char next = prefix.charAt(1);
            return this.c == c && 
                this.adjacent.containsKey(next) && 
                this.adjacent.get(next).startsWith(prefix.substring(1, prefix.length()));
        }
    }

    public Trie() {
        this.roots = new HashMap<>();
    }
    
    public void insert(String word) {

        char c = word.charAt(0);
        if (!this.roots.containsKey(c)) {
            this.roots.put(c, new TrieNode(c));
        }

        String strToInsert = word.substring(1, word.length()) + END_OF_WORD;
        this.roots.get(c).insert(strToInsert);
    }
    
    public boolean search(String word) {
        char c = word.charAt(0);
        String strToSearch = word + END_OF_WORD;
        return this.roots.containsKey(c) && this.roots.get(c).search(strToSearch);
    }
    
    public boolean startsWith(String prefix) {
        char c = prefix.charAt(0);
        String strToSearch = prefix + END_OF_WORD;
        return this.roots.containsKey(c) && this.roots.get(c).startsWith(strToSearch);
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */