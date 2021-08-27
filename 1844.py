class Solution:
    def shift(self,c,x):
        alp='abcdefghijklmnopqrstuvwxyz'
        c=c.lower()
        ind1=alp.index(c)
        ind2=(ind1+x)%26
        return alp[ind2]
    
    def replaceDigits(self, s: str) -> str:
        #letters #numbers
        st=''
        for t in range(0,len(s)):
            if t%2==1:
                st=st+self.shift(s[t-1],int(s[t]))
            else:
                st=st+s[t]
        return st