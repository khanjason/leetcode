class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store={}

    def insert(self, key: str, val: int) -> None:
        self.store[key]=val

    def sum(self, prefix: str) -> int:
        tot=0
        for i in self.store.keys():
            if i.startswith(prefix):
                tot=tot+self.store[i]
        return tot


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
