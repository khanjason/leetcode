class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct=[]
        for i in nums:
            if i not in distinct:
                distinct.append(i)
        
        s=sorted(distinct)
        if len(s)<3:
            return max(s)
        return s[len(s)-3]
