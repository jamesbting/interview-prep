class StockSpanner:

    def __init__(self):
        self.price_history = []

    def next(self, price: int) -> int:
        span = 1
        last_span = 0
        while self.price_history and self.price_history[-1][0] <= price:
            curr = self.price_history.pop()
            last_span = curr[1]
            span += last_span
        
        self.price_history.append((price, span))
        return span
        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)