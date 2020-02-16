class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        finlist=[]
        for t in range(0,len(nums),2):
            for times in range(0,nums[t]):    
                finlist.append(nums[t+1])
            
        return(finlist)
