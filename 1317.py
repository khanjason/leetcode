class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        c=n
        while c!=0:
            c=c-1
            b=n-c
            if '0' not in str(b) and '0' not in str(c):
                return [b,c]
