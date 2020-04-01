class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for t in range(0,len(nums)):
            if t==(len(nums)-1):
                return False
            
            if nums[t]==nums[t+1]:
                return True
