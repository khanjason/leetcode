class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
   
        piles=sorted(piles)
        piles=piles[::-1]
        tot=0
        c=(len(piles)/3)
        i=1
        while (i<len(piles)) and (c>0):
            
           
            tot=tot+piles[i]
            i=i+2
            c=c-1
        return(tot)
