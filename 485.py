class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tot=0
        maxx=0
        for i in nums:
            if tot>maxx:
                maxx=tot
            
            if i!=1:
                tot=0
            else:
                tot=tot+1
        if tot>maxx:
                maxx=tot
        return (maxx)
