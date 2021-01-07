class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums=sorted(nums)
        x=len(nums)
        while x!=0:
            
            count=0
            for i in nums:
                if i>=x:
                    count=count+1
            if count==x:
                return x
            x=x-1
        
        return -1
