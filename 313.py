class Solution(object):
    
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        ugs=[1]
        hep=[]
        for p in primes:
            hep.append((p,0))
        for r in range(1, n): 
            ugs.append(hep[0][0])
            while ugs[-1]==hep[0][0]: 
                val, i = heappop(hep)
                val = val//(ugs[i]) * ugs[i+1]
                heappush(hep, (val, i+1))
        return ugs[-1]
        
        
