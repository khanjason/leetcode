class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if sum(nums[:i+1])==sum(nums[i:]):
                return i
        return -1
