class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        ans=[]
        for i in range(0,len(groupSizes)):
            if groupSizes[i] not in d.keys():
                d[groupSizes[i]]=[i]
            else:
                d[groupSizes[i]].append(i)
        
        for k,v in d.items():
            prev=0
            for i in range(0,len(v)+1,k):
                if v[prev:i]!=[]:
                    ans.append(v[prev:i])
                prev=i
            
        return ans
        
