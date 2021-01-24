class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            tot=0
            for t in str(i):
                tot=tot+int(t)
            if tot not in d.keys():
                d[tot]=1
            else:
                d[tot]+=1
        maxx=0
        for k,v in d.items():
            if v>maxx:
                maxx=v
        count=0
        for k,v in d.items():
            if v==maxx:
                count+=1
        return count
