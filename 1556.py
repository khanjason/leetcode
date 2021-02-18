class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=str(n)
        if len(s)<4:
            return s
        r=s[::-1]
        st=''
        c=1
        for t in range(0,len(r)):
            if c%3==0:
                st=st+r[t]
                st=st+'.'
            else:
                st=st+r[t]
            c+=1
            
        ans=(st[::-1])
        if ans[0]=='.':
            ans=ans[1:]
        return ans
