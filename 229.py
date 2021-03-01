class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k=int(len(nums)//3)
        
        nums=sorted(nums)
        ans=[]
        prev=''
        count=0
        for i in range(0,len(nums)):
            if i==0:
                if len(nums)==1:
                    ans.append(nums[0])
                    return ans
                prev=nums[0]
                count=count+1
            else:
                if nums[i]==prev:
                    count=count+1
                else:
                    if count>k:
                        ans.append(prev)
                    count=1
                    prev=nums[i]
        if count>k:
            ans.append(prev)
            count=1
            prev=nums[i]
        return ans
                        
