class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        medals=["Gold Medal","Silver Medal","Bronze Medal"]
        s=sorted(nums)
        if len(nums)<3:
            t=len(nums)+1
        else:
            t=4
            
        #relative - len-nums(score-1)
        for i in range(1,t):
            m=max(nums)
            ind1=nums.index(m)
            nums[ind1]=-i
           
        
        for item in nums:
            if item>=0:
                ind2=nums.index(item)
                sortind=s.index(item)
                nums[ind2]=str(len(nums)-(sortind))
        for n in range(1,t):
            
            ind=nums.index(-n)
            nums[ind]=medals[n-1]
        
        return(nums)
