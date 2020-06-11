from itertools import combinations_with_replacement
class Solution:
    
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        lenn=target//min(candidates)
        for n in range(1,lenn+1):
            subs=combinations_with_replacement(candidates,n)
            for i in list(subs):
                if sum(i)==target:
                    res.append(list(i))
        return res
