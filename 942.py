class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N=len(S)
        iarray=[]
        darray=[]
        A=[]
        for i in range(0,N+1):
            iarray.append(i)
        for d in range(N,-1,-1):
            darray.append(d)
        for t in range(0,len(S)):
            if S[t]=='I':
                A.append(iarray[0])
                del iarray[0]
            if S[t]=='D':
                A.append(darray[0])
                del darray[0]
        A.append(darray[0])
        
        return A
