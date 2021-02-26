class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #units - 9     0-9  total 10   n=0  0
        #tens - 91   10-99 total 89  n=1     9
        #hundres - 739 100-999  899   n=2    160
        #maxunit - one unit below max
        #n=pow(10,n)
        maxunit=n
        print(maxunit)
        if maxunit==0:
            return 1
        
        if maxunit==1:
            return 10
        tot=9
        done=0
        for i in range(1,n):
            tot*=9-done
            done=done+1
        return tot + self.countNumbersWithUniqueDigits(n-1)
