class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for item in nums:
            if len(str(item))%2==0:
                c=c+1
        return(c)
