class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        p1=1
        p2=1
        c=0
        while p1<len(nums) and p2< len(nums):
            if nums[p2]==nums[p2-1]:
                p2+=1
            else:
                nums[p1]=nums[p2]
                p1+=1
                p2+=1
                c+=1
        return c+1
        
    
