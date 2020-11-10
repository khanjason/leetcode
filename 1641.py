class Solution:
    def countVowelStrings(self, n: int) -> int:
        c1=1
        c2=1
        c3=1
        c4=1
        c5=1
        tot=0
        
        for i in range(n):
            c1=c1+c2+c3+c4+c5
            c2=c2+c3+c4+c5
            c3=c3+c4+c5
            c4=c4+c5
            c5=c5
            
        return c1
