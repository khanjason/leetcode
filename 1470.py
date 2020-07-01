class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length=len(nums)
        midpoint=int(len(nums)/2)
        half1=nums[:midpoint]
        half2=nums[midpoint:]
        ans=[]
        
        for i in range(0,len(half1)):
            ans.append(half1[i])
            ans.append(half2[i])
        return ans
            
