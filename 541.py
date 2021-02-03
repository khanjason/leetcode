class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        y=2*k
        if len(s)<y and len(s)>=k:
            t=s[:k]
            t=t[::-1]
            
            s=t+s[k:]
            
            return s
        for i in range(0,len(s),y):
            
            tmp=s[i:i+k]
            tmp=tmp[::-1]
            s=s[:i]+tmp+s[i+k:]
        return s
