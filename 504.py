class Solution:
    def convertToBase7(self, num: int) -> str:
        stri=""
        minn=False
        if num<0:
            minn=True
            num=abs(num)
        while num>=7:
            n= num % 7
            stri=stri+str(n)
            num=int(num//7)
        stri=stri+str(num)
        if minn==True:
            stri=stri+'-'
        return(stri[::-1])
            
                
