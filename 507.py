class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=0:
            return False
        divs=[]
        ssum=0
        sq= int(num**0.5)
        for i in range(1,sq+1):

            if num % i==0:
                ssum=ssum+i
                if (i*i)!=num:
                    ssum=ssum+(num/i)
        if ssum-num==num:
            return True
        return False
