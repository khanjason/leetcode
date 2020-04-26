class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        prev=0
        nums=sorted(nums)
        dups=[]
        for i in range(0,len(nums)):
            if i==0:
                prev=nums[i]
            else:
                if nums[i]==prev:
                    dups.append(nums[i])
                prev=nums[i]
        return dups
