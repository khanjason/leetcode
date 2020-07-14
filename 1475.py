class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        newarr=[]
        for i in range(0,len(prices)):
            jays=[]
            for j in range(0,len(prices)):
                
                if j>i and prices[j]<=prices[i]:
            
                    jays.append(j)
                    
            if len(jays)>0:
                newarr.append(prices[i]-prices[min(jays)])
            else:
                newarr.append(prices[i]-0)
        return newarr
