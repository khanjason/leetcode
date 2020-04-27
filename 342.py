class Solution:
    def divfour(self,n):
        while n>4:
            if n % 4==0:
                n=int(n//4)
            else:
                return False
        if n==4:
            return True
        else:
            return False
    
    def isPowerOfFour(self, num: int) -> bool:
        if num==1:
            return True
        if num % 4==0:
            return self.divfour(num)
        return False
