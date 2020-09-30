class Solution(object):
    def sub_lists(self,L): 
           
        return [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        tot=0
        lists=self.sub_lists(arr)
        
        for l in lists:
            
            if len(l)%2==1:
                
                tot=tot+sum(l)
        return tot
