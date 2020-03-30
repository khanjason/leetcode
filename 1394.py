class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucks=[]
        sorts=sorted(arr)
        done=[]
        c=0
        target=sorts[0]
        for i in range(0,len(sorts)):
            if sorts[i] not in done:
                if c==target:
                    lucks.append(target)
                target=sorts[i]
                c=1
                done.append(sorts[i])
            else:
                c=c+1
                
        if c==target:
                lucks.append(target)
        if lucks!=[]:
            return max(lucks)
        return -1
            
