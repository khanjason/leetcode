class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(0,n):
            nums.append(start+(2*i))
        print(nums)
        xor = 0
        for t in range(0,n): 
            xor=xor^nums[t] 
        return xor
