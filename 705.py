class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set=[]

    def add(self, key: int) -> None:
        
        self.set.append(key)
    def remove(self, key: int) -> None:
        self.set = list(filter(lambda a: a != key, self.set))
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        
        if key in self.set:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
