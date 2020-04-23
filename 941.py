class Solution:
    def checkduplicate(self,arr):
        for i in arr:
            if arr.count(i)>1:
                return True
        return False
            
    
    
    def validMountainArray(self, A: List[int]) -> bool:
        if A==[]:
            return False
        
        peak=int(A.index(max(A)))
        
        left=A[:peak+1]
        
        right=A[peak:]
        
        if self.checkduplicate(left):
            return False
        if self.checkduplicate(right):
            return False
        
        
        if len(left)<2 or len(right)<2:
            return False
        if sorted(left) ==left:
            revr=right[::-1]
            if revr==sorted(right):
                return True
        return False
