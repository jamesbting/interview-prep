class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters_set = set(string.ascii_lowercase)
        
        return set(sentence) == letters_set