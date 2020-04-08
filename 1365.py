class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr2=[]
        for i in nums:
            c=0
            for t in nums:
                if t<i:
                    c=c+1
            arr2.append(c)
        return arr2
