class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        p1=int(len(nums)/2)
        p2=int(len(nums)/2)-1
        print(p1)
        print(p2)
        for i in range(int(len(nums)/2)+1):
            if nums[p1] not in s:
                s.add(nums[p1])
            else:
                return nums[p1]
            if nums[p2] not in s:
                s.add(nums[p2])
            else:
                return nums[p2]
            p1=p1+1
            p2=p2-1
