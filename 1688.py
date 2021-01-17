class Solution:
    def numberOfMatches(self, n: int) -> int:
        tot=0
        while n>1:
            if n%2==0:
                tot=tot+(n/2)
                n=int(n/2)
            else:
                tot=tot+((n-1)/2)
                n=int(((n-1)/2)+1)
        return int(tot)
            
