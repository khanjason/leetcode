class RecentCounter:

    def __init__(self):
        self.timings=[]

    def ping(self, t: int) -> int:
        if self.timings==[]:
            self.timings.append(t)
            return len(self.timings)
        if t>(self.timings[0]+3000):
            self.timings.append(t)
            while t>(self.timings[0]+3000):
                self.timings=self.timings[1:]
                
                
            
        elif t > (self.timings[-1]-3000):
            self.timings.append(t)
       
        
        return len(self.timings)
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
