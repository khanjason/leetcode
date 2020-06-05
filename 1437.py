class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cur=float("inf")
        for i,n in enumerate(nums):
            if n==0:
                cur=cur+1
            else:
                if cur<k:
                    return False
                cur=0
                
        return True
