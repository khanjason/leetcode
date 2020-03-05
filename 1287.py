class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter=int(len(arr)/4)
        tot=0
        for i in range(0,len(arr)):
            
            
            if tot>=quarter:
                return arr[i]
            elif i==(len(arr)-1):
                break
            elif arr[i]==arr[i+1]:
                tot=tot+1
            else:
                tot=0
            
