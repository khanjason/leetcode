from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store=defaultdict(list)
        self.times=defaultdict(list)
        #key__timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.store[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        x=self.times[key]
        low=0
        high=len(x)-1
        while low<high:
            mid=(low + high)//2+1    
            if x[mid]>timestamp:
                high=mid-1
            else:
                low=mid
        if x[low]<=timestamp:
            return self.store[key][low]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
