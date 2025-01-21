class SeatManager:

    def __init__(self, n: int):
        self.seat_heap = []
        self.marker = 1
        

    def reserve(self) -> int:
        if self.seat_heap:
            return heapq.heappop(self.seat_heap)
        
        ans = self.marker
        self.marker += 1
        return ans
        

    def unreserve(self, seatNumber: int) -> None:
        return heapq.heappush(self.seat_heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)