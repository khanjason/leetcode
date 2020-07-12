class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs=0
        for i in range(0,len(nums)):
            for j in nums[i+1:]:
                if nums[i]==j:
                    pairs=pairs+1
        return pairs
