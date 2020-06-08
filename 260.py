class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c=0
        seen=set()
        correction=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                correction.add(i)
        return(list(seen.symmetric_difference(correction)))
