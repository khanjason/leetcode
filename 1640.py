class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        #arr is a target
        #put pieces together to get arr
        p1=0
        p2=1
        found=False
        while p1!=len(arr):
            for item in pieces:
                found=False
                print(arr[p1])
                print(item[0])
                if arr[p1]==item[0]:
                    
                    found=True
                    for i in range(0,len(item)):
                        if item[i]!=arr[p1]:
                            return False
                        p1=p1+1
                        if p1==len(arr)-1:
                            return True
                    break
            if found==False:
                return False
        return True
