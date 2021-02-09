class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d={}
        for i in range(lowLimit,highLimit+1):
            t=str(i)
            tot=0
            for s in t:
                tot+=int(s)
            if tot in d.keys():
                d[tot]+=1
            else:
                d[tot]=1
        d=sorted(d.items() ,key=lambda item: item[1],reverse=True)
        return d[0][1]
