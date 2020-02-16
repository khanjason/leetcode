class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        li=[]
        tot=1
        for t in str(n):
            li.append(int(t))
            tot=tot*int(t)
        s=sum(li)
        return(tot-s)
