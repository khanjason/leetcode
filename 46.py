from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p=permutations(nums)
        ans=[]
        for c in list(p):
            ans.append(list(c))
        return ans
