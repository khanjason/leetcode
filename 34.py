class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos=[]
        for item in nums:
            if item==target:
                pos.append(nums.index(item))
                nums[nums.index(item)]='a'
        
        if pos!=[]:
            if len(pos)==1:
                pos=list((pos[0],pos[0]))
            else:
                pos=list((pos[0],pos[-1]))
            return pos
        
        else:
            return [-1,-1]
