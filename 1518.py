
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        if numExchange>numBottles:
            return numBottles
        tot=0
        left=0
        
        
        while numBottles>0:
            tot=tot+numBottles
            tmp=int((numBottles+left)/numExchange)
            left=(numBottles+left)%numExchange
            numBottles=tmp
        return(tot)
    
   
