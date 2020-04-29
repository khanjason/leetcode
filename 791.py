class Solution:
    def customSortString(self, S: str, T: str) -> str:
        #encode into numbers
        alp=[]
        for let in range(0,len(S)):
            alp.append(let)
        #encode the T
        #sort
        #decode
        overflow=[] #if not in S
        Tlist=[]
        for l in T:
            if l in S:
                Tlist.append(S.find(l))
            else:
                overflow.append(l)
        sortedT=sorted(Tlist)
        newT=[]
        for i in sortedT:
            ind=alp.index(i)
            newT.append(S[ind])
        ans=(''.join(newT+overflow))
        #print(ans)
        return ans
