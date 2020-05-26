class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)
        for n in range(0,len(nums)):
            for i in range(0,len(nums)-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
        return(nums)
