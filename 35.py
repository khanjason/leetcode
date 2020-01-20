class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        clone=nums
        counter=0
        for item in nums:
            counter=counter+1
            if item==target:
                return nums.index(target)
            elif counter==length:
                clone.append(target)
                clone.sort()
                return clone.index(target)
