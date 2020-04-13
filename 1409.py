class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P=[]
        outp=[]
        for t in range(1,m+1):
            P.append(t)
        for i in range(0,len(queries)):
            pos=P.index(queries[i])
            outp.append(pos)
            while pos!=0:
                P[pos],P[pos-1]=P[pos-1],P[pos]
                pos=P.index(queries[i])
        return(outp)
