class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j:
                    if ((nums[i]-1)*(nums[j]-1))>maxi:
                        maxi=((nums[i]-1)*(nums[j]-1))
        return maxi
