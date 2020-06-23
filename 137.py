class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        done=set()
        big=set()
        for i in nums:
            if i in done:
                big.add(i)
            else:
                done.add(i)
        return(big.symmetric_difference(done)).pop()
