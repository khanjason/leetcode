class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            for x in nums:
                if x==val:
                    nums.remove(x)
                
        return len(nums)
