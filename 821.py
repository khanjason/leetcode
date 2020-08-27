class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        times=S.count(C)
        start=S
        li=[]
        res=[]
        for i in range(0,len(S)):
            if S[i]==C:
                li.append(i)
        
        for t in range(0,len(S)):
            tmp=[]
            for n in li:
                tmp.append(abs(t-n))
            res.append(min(tmp))
        return(res)
