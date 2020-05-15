class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        leng=len(nums)
        if leng>1:
            r=0
            w=0
            b=0
            for i in nums:
                if i==0:
                    r=r+1
                if i==1:
                    w=w+1
                if i==2:
                    b=b+1


            ind=0

            for t in range(0,r):
                nums[t]=0
            ind=ind+(r)
            
            
            for p in range(ind,ind+w):
                nums[p]=1
            ind=ind+(w)
            for x in range(ind,ind+b):
                nums[x]=2
