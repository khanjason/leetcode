class Solution:
 
    
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        Bs={0}
        ans=set()
        for i in A:
            Bs = {i | y for y in Bs} | {i}
            ans|= Bs
        return len(ans)
            
  
