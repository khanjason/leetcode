class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mi=min(nums)
        ma=max(nums)
        for i in range(mi,0,-1):
            if ma%i==0:
                if mi%i==0:
                    return i