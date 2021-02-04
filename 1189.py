class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #b =1
        #a =1
        #l= 2
        #o=2
        #n=1
        bcount=text.count('b')
        acount=text.count('a')
        ncount=text.count('n')
        
        m=min(bcount,acount,ncount)
        if m==0:
            return m
        needed=2*m
        while m!=0:
            if text.count('l') >= needed and text.count('o')>=needed:
                return m
            else:
                needed=needed-2
                m-=1
        return m
