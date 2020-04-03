class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s=''
        for i in A:
            s=s+str(i)
        a=int(s)
        tot=str(a+K)
        ret=[]
        for t in tot:
            ret.append(int(t))
        return ret
