
class Solution:
    def checkarith(self,li):
        if len(li)<2:
            return False
        s=sorted(li)
        for i in range(len(s)-1):
            if (s[i+1] - s[i] != s[1] - s[0]):
                return False
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            tmp=nums[l[i]:r[i]+1]
            ans.append(self.checkarith(tmp))
        return ans
