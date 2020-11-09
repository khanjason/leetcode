class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        while count<=len(nums)-3:
            if nums[count]==nums[count+2]:
                del(nums[count])
            else:
                count=count+1
        return len(nums)
