class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        stack_of_words = s.split(' ')
        ans = ''
        while stack_of_words:
            curr_word = stack_of_words.pop(len(stack_of_words) - 1)
            if (curr_word == ''):
                continue
            ans = ans + curr_word
            if len(stack_of_words) > 0:
                ans = ans + ' '
        return ans.strip()