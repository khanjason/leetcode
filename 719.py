class Solution:
    def possible(self,guess,nums,k):
            left=0
            c=left 
            
            for right, x in enumerate(nums):
                while x-nums[left]>guess:
                    left=left+1
                c=c+right-left
            if c>=k:
                return True
            return False

    
    def smallestDistancePair(self, nums, k):
        nums=sorted(nums)
        low=0
        high=nums[-1]-nums[0]
        while low<high:
            mid=(low+high)/ 2
            if self.possible(mid,nums,k):
                high=mid
            else:
                low=mid+1

        return int(low)
