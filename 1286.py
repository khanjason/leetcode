from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs=list(combinations(characters,combinationLength))
        self.callcount=0
        
            
        

    def next(self) -> str:
        self.callcount=self.callcount+1
        
        
        x=((self.combs))[self.callcount-1]
        return ''.join(x)
        
    def hasNext(self) -> bool:
        if self.callcount<len(self.combs):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
