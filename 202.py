class Solution:
    def isHappy(self, n: int) -> bool:
        done=[]
        while True:
            if n==1:
                return True
            
            s=str(n)
            
            n=0
            for i in s:
                sq=int(i)**2
                n=n+sq
            
            if n in done:
                return False
            done.append(n)
            
