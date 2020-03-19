class Solution:
    def tobin(self,n):
        s=''
        while n>0:
            if n % 2==1:
                s=s+'1'
                n=int(n/2)
            else:
                s=s+'0'
                n=int(n/2)
        
        return s
    def hammingWeight(self, n: int) -> int:
        return((self.tobin(n)).count('1'))
