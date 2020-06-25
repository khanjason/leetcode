class Solution:
    def bintodec(self,b):
        
        s=b[::-1]
        c=1
        tot=0
        for i in s:
            if i=='1':
                tot=tot+c
            c=c*2
        print(tot)
        return (tot)
    
    def numSteps(self, s: str) -> int:
        steps=0
        n=self.bintodec(s)
        while n!=1:
            if n%2:
                n=n+1
            else:
                n=n//2
            steps=steps+1
           
        return steps
