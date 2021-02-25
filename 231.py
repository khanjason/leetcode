class Solution:
    def divtwo(self,n):
        while n>2:
            if n % 2==0:
                n=int(n//2)
            else:
                return False
        if n==2:
            return True
        else:
            return False
    

    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n % 2==0:
            return self.divtwo(n)
        return False
    
