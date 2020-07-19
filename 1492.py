class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        li=[]
        start=1
        while start!=n+1:
            if n%start==0:
                li.append(start)
            start=start+1;
       
        if len(li)<k:
            return -1
        return li[k-1]
