class Solution:
    def compress(self, chars: List[str]) -> int:

        i, end = 0, 0
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1


            chars[end] = letter
            end += 1

            if count > 1:
                for c in str(count):
                    chars[end] = c
                    end += 1

        return end