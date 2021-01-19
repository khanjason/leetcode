class OrderedStream:

    def __init__(self, n: int):
        self.heap=[]
        self.ptr=0
        for i in range(n):
            self.heap.append([])

    def insert(self, id: int, value: str) -> List[str]:
        self.heap[id-1]=value
        ans=[]
        
        while self.heap[self.ptr] !=[]:
            ans.append(self.heap[self.ptr])
            if self.ptr==len(self.heap)-1:
                break
            self.ptr+=1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
