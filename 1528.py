class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        slist=[]
        newlist=[0]*len(s)
        for t in s:
            slist.append(t)

        for i in range(0,len(slist)):
                newlist[indices[i]]=slist[i]
        return(''.join(newlist))
