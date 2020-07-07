class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        
        if N<=2:
            return 1
        
        start=1
        start2=1
        for i in range(0,N-2):
            f=(start)+(start2)
            start=start2
            start2=f
            
        return start2
