class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot=len(nums)
        numlist=sorted(nums)
        c=-1
        for i in numlist:
            c=c+1
            if i !=c:
                return c
        return c+1
