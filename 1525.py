from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        d=defaultdict(int)
        c=1
        for i in s:
            d[i]+=c
        count=0
        b=defaultdict(int)
        for i in range(0,len(s)):
            b[s[i]]+=c
            d[s[i]]-=c
            if d[s[i]]==0:
                del d[s[i]]
            if len(b) ==len(d):
                count=count+1
            elif len(b)>len(d):
                break
        return count
