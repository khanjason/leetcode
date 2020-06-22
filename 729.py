class MyCalendar:

    def __init__(self):
        self.starts=[]
        self.ends=[]

    def book(self, start: int, end: int) -> bool:
        for i in range(0,len(self.starts)):
            if start==self.starts[i] or (start>self.starts[i] and start<self.ends[i]):
                return False
            if end>self.starts[i] and start<self.starts[i]:
                return False
        self.starts.append(start)
        self.ends.append(end)
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
