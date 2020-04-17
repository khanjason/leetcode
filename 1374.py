class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==1:
            s= 'a' * n
            return s
        else:
            s= 'a' * (n-1)
            s=s+'b'
            return s
