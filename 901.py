class StockSpanner:

    def __init__(self):
        self.prev=[]
        self.curr=0

    def next(self, price: int) -> int:
        if self.prev==[]:
            self.prev.append((price,1))
            return 1

        return self.consec(price)
    def consec(self,price):
        if self.prev[-1][0]<=price:
            count=1
            while len(self.prev)!=0 and self.prev[-1][0]<=price:
                p= self.prev.pop()
                count=count+p[1]
            self.prev.append((price,count))
            return count
        else:
            self.prev.append((price,1))
            return 1
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

