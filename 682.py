class Solution:
    def calPoints(self, ops: List[str]) -> int:
        valid=[]
        s=0
        for n in ops:
            if n=='C':
                can=valid.pop()
                s=s-can
            elif n=='D':
                doub=((valid[len(valid)-1])*2)
                valid.append(doub)
                s=s+doub
            elif n=='+':
                plus=((valid[len(valid)-1])+(valid[len(valid)-2]))
                valid.append(plus)
                s=s+plus
            
            else:
                i=int(n)
                valid.append(i)
                s=s+i
        return s
