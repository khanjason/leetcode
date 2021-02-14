import math
class Solution:
    
    def primeFactors(self,n,s): 

        while n % 2 == 0: 
            s.add(2)
            n = n / 2
        for i in range(3,int(math.sqrt(n))+1,2): 

            while n % i== 0: 
                s.add(int(i))
                n = n / i 

        if n > 2: 
            s.add(int(n))
        return s
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        se={2,3,5}
        s=self.primeFactors(num,set())
        #print(s)
        if s.issubset(se):
            return True
        else:
            return False
