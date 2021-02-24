from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        nums=[]
        for i in range(1,10):
            nums.append(i)
        comb=combinations(nums,k)
        for t in list(comb):
            if sum(t)==n:
                ans.append(list(t))
        return ans
