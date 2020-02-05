class Solution:
    def arrangeCoins(self, n: int) -> int:
        curr=0
        coin='¤'
        tot=n
        if n==1 or n==0:
            return n
        
        for i in range(1,n+1):
            
            if tot<i:
                i=i-1
                return i
            #print(i*coin)
            tot=tot-i
