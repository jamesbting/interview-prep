class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        changingNums = set()

        for i, n in enumerate(change):
            if n >= i:
                changingNums.add(i)

        print(changingNums)
        changed = False
        ans = ''

        for i in range(len(num)):
            n = int(num[i])
            if n < change[n]:
                changed = True
                ans += str(change[n])
            elif n > change[n] and changed:
                ans += num[i:]
                break
            else:
                ans += num[i]
            i += 1
        return ans