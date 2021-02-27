class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            if arr[i]*2 in arr:
                ind=arr.index(arr[i]*2)
            
                if ind!=i:
                    return True
