class Solution:
    def tobin(self,n):
        lastzero=False
        lastone=False
        while n>=1:
        
            if n%2==0:
                #add 0
                print(0)
                if lastzero==True:
                    return False
                else:
                    lastzero=True
                    lastone=False
                    n=int(n//2)
            if n % 2==1:
                #add 1
                
                if lastone==True:
                    return False
                else:
                    lastone=True
                    lastzero=False
                    n=int(n//2)
        return True
    def hasAlternatingBits(self, n: int) -> bool:
        if n<2:
            return True
        return self.tobin(n)
