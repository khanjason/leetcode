class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        for item in nums1:
            if item in nums2 and item not in inter:
                inter.append(item)
        return inter
