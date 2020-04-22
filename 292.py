class Solution:
    def canWinNim(self, n: int) -> bool:
        #you first
        
        if n%4==0:
            return False
        return True
    
        #if remainder less tahn 4, return false
        #keep diving by 3
