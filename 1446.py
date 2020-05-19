class Solution:
    def maxPower(self, s: str) -> int:
        m=1
        pows=[]
        for i in range(0,len(s)):
            if i==0:
                prev=s[i]
            elif s[i]==prev:
                m=m+1
            else:
                pows.append(m)
                m=1
                prev=s[i]
        pows.append(m)
        return max(pows)
