class Solution:
    def checkarith(self,li):
        if len(li)<2:
            return False
        s=sorted(li)
        for i in range(len(s)-1):
            if (s[i+1] - s[i] != s[1] - s[0]):
                return False
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        return self.checkarith(arr)
