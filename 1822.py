class Solution:
    def signFunc(self,x):
        if x>0:
            return 1
        if x<0:
            return -1
        else:
            return 0

    def arraySign(self, nums: List[int]) -> int:
        tot=1
        for i in nums:
            tot=tot*i
        return self.signFunc(tot)