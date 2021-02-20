class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tot=0
        for t in set(nums):
            if nums.count(t)==1:
                tot+=t
        return tot
