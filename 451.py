class Solution:
    def frequencySort(self, s: str) -> str:
        chars=set()
        d=dict()
        for i in s:
            if i not in chars:
                chars.add(i)
                d[i]=1
            else:
                d[i]=d[i]+1
        li=(sorted(d.items(), key=lambda x: x[1], reverse=True))
        ans=''
        for tup in li:
            for n in range(0,tup[1]):
                ans=ans+tup[0]
        return ans
