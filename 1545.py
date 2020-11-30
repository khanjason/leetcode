class Solution:
    def invert(self,s):
        a=''
        for item in s:
            if item=='1':
                a=a+'0'
            else:
                a=a+'1'
        return a
    def findKthBit(self, n: int, k: int) -> str:
        i=0
        s='0'
        while i!=n:
            s=s+'1'+self.invert(s)[::-1]
            i=i+1
        return(s[k-1])
