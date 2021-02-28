class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        t=''
        prev=''
        if len(nums)==1:
            return nums[0]
        
        for y in range(0,len(nums)):
            if y==0:
                prev=nums[y]
            else:
                if nums[y]==prev:
                    t=prev
                    prev=nums[y]
                else:
                    if t!=prev:
                        return prev
                    else:
                        prev=nums[y]
        return prev
