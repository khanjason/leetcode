class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        m=max(A)
        return A.index(m)
