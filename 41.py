class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        c=1
        for i in nums:
            if i==c:
                c=c+1
        return c
