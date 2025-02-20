class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""

        lst = self.mp[key]
        if timestamp < lst[0][0]:
            return ""
        
        left = 0
        right = len(lst)

        while left < right:
            mid = (left + right) // 2
            if lst[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if right == 0 else lst[right - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)