class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runs=[]
        tot=0
        for i in nums:
            tot=tot+i
            runs.append(tot)
        return runs
