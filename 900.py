class RLEIterator:
#a[i]= number of times a[i+1] is repeated
    def __init__(self, A: List[int]):
        self.initi=A[::-1]
        
    def next(self, n: int) -> int:
        curr=0
        while curr<n:
            if not self.initi:
                return -1
            times=self.initi.pop()
            num=self.initi.pop()
            curr=curr+times
        if curr>n:
            self.initi.append(num)
            self.initi.append(curr-n)
        return num
        
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)

