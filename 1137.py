class Solution:
    def tribonacci(self, n: int) -> int:
        if n==1 or n==2:
            return 1
        
        start=0
        start2=1
        start3=1
        c=2
        tot=0
        while c<n:
            c=c+1
            tot=start+start2+start3
            start=start2
            start2=start3
            start3=tot
            
        return tot
            
